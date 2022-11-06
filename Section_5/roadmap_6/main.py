from typing import Optional
import pandas as pd

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

@api.get('/api/sustain/{city}')
def greencity(city: str, factor: Optional[str] = 'overall') -> dict:
    msg ={'city':city, 'info': None}
    report = _get_external_report(city, factor)
    if report:
        msg = {
            'country': report.get('country'),
            'city': city,
            factor: int(report.get(factor))
        }
    return msg


def _get_external_report(city: str, factor: Optional[str]="overall"):
    df = pd.read_csv("greencities.csv")
    df.index = df.city.apply(lambda x: x.lower().replace(' ','_'))
    resp = {}
    if city in df.index:
        resp = {
            'country': df.loc[city]['Country'],
            'people': df.loc[city]['People'],
            'planet': df.loc[city]['Planet'],
            'profit': df.loc[city]['Profit'],
            'overall': df.loc[city]['Overall']
        }
    return resp

if __name__ == "__main__":
    uvicorn.run('main:api', port=8000, host='127.0.0.1', reload=True)
