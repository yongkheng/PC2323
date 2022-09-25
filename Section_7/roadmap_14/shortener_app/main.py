# shortener_app/main.py

import secrets
import validators
import string
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from sqlalchemy.orm import Session
from . import models
from .database import SessionLocal, engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates("./shortener_app")


def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)


def raise_not_found(request):
    message = f"URL '{request.url}' doesn't exist"
    raise HTTPException(status_code=404, detail=message)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/url")
async def create_url(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    form = dict(form)
    url = form["url"]
    if not validators.url(url):
        raise_bad_request(message="Your provided URL is not valid")

    chars = string.ascii_uppercase + string.digits
    key = "".join(secrets.choice(chars) for _ in range(5))
    db_url = models.URL(target_url=url, key=key)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    url_short = f"http://127.0.0.1:8000/{key}"
    return templates.TemplateResponse(
        "link.html",
        {
            "request": request,
            "url": url,
            "url_short": url_short,
        },
    )


@app.get("/{url_key}")
def forward_to_target_url(
    url_key: str, request: Request, db: Session = Depends(get_db)
):
    db_url = db.query(models.URL).filter(models.URL.key == url_key).first()
    if db_url:
        return RedirectResponse(db_url.target_url)
    else:
        raise_not_found(request)
