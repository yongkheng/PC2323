from typing import Optional
from pydantic.main import BaseModel

class Query(BaseModel):
    city: str
    factor: Optional[str] = 'overall'