from starlette.requests import Request
from starlette.templating import Jinja2Templates
from fastapi import APIRouter

templates = Jinja2Templates('templates')

router = APIRouter()

@router.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
