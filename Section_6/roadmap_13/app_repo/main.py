import json

import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

from api import greencity_api
from views import index

api = fastapi.FastAPI()

def load_env():
    with open('settings.json') as f:
        env = json.load(f)
    return env

def configure():
    api.mount('/static', StaticFiles(directory='static'), name='static')
    api.include_router(greencity_api.router)
    api.include_router(index.router)
    env = load_env()
    print(env['setting'])

if __name__ == "__main__":
    configure()
    uvicorn.run('main:api', port=8000, host='127.0.0.1', reload=True)
else:
    configure()
