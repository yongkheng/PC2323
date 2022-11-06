from starlette.responses import JSONResponse
from infrastructure.greencity import _get_external_report
from models.query import Query
from fastapi import Depends, APIRouter

router = APIRouter()


@router.get('/api/sustain/{city}')
async def greencity(query: Query = Depends()) -> JSONResponse:
    msg = {'city': query.city, 'info': None}
    report = await _get_external_report(query.city, query.factor)
    if report:
        msg = {
            'country': report.get('country'),
            'city': query.city,
            query.factor: int(report.get(query.factor))
        }
    return JSONResponse(msg, status_code=200)
