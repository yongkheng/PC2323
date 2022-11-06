from datetime import datetime
from typing import List

post_data = {
    'post_id': '123',
    'author': 'John Smith',
    'msg': 'Hello World',
    'reviews': [5, 4, '3']
}

class Post:
    def __init__(self, post_id: int, author: str, msg: str,
                 reviews: List[int]):
        self.post_id = post_id
        self.author = author
        self.msg = msg
        self.reviews = reviews

    def __str__(self):
        return str(self.__dict__)

post = Post(**post_data)
print(post)

