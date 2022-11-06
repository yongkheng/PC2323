from typing import Optional
import pandas as pd

async def _get_external_report(city: str, factor: Optional[str] = "overall"):
    df = pd.read_csv("greencities.csv")
    df.index = df.city.apply(lambda x: x.lower().replace(' ', '_'))
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
