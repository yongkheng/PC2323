from pydantic import BaseModel

from datetime import datetime
from typing import List

post_data = {
    'post_id': '123',
    'author': 'John Smith',
    'msg': 'Hello World',
    'reviews': [5, 4, '3']
}

class Post(BaseModel):
    post_id: int
    author: str
    msg: str
    reviews: List[int]

post1 = Post(**post_data)
post2 = Post(**post_data)
print(post1)
print(post1 == post2, post1 is post2)
