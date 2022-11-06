import fastapi
import uvicorn
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

api = fastapi.FastAPI()
templates = Jinja2Templates('.')

api.mount('/static', StaticFiles(directory='static'), name='static')

@api.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

if __name__ == "__main__":
    uvicorn.run('main:api', port=8000, host='127.0.0.1', reload=True)