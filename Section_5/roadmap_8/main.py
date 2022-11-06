from typing import Optional
import pandas as pd

import fastapi
import uvicorn
from pydantic.main import BaseModel
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

api = fastapi.FastAPI()
templates = Jinja2Templates('.')

api.mount('/static', StaticFiles(directory='static'), name='static')

@api.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

class Query(BaseModel):
    city: str
    factor: Optional[str] = 'overall'

@api.get('/api/sustain/{city}')
async def greencity(query: Query=fastapi.Depends() ) -> dict:
    msg ={'city':query.city, 'info': None}
    report = await _get_external_report(query.city, query.factor)
    if report:
        msg = {
            'country': report.get('country'),
            'city': query.city,
            query.factor: int(report.get(query.factor))
        }
    return msg


async def _get_external_report(city: str, factor: Optional[str]="overall"):
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
