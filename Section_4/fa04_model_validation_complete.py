from datetime import datetime
from dateutil.parser import parse
from typing import List, Optional, Union

post_data = {
    'post_id': '123',
    'author': 'John Smith',
    'msg': 'Hello World',
    'reviews': [5, 4, '3']
}


class Post:

    def __init__(self, post_id: int, author: str, msg: str,
                 reviews: Optional[Union[None, List[int]]]):

        if reviews is None:
            reviews = []

        try:
            self.post_id = int(post_id)
        except ValueError:
            raise Exception("Invalid post_id, it must be an integer.")

        try:
            self.author = str(author)
        except ValueError:
            raise Exception("Invalid author, it must be a string.")

        try:
            self.msg = str(msg)
        except ValueError:
            raise Exception("Invalid msg, it must be a string.")

        try:
            self.reviews = [int(p) for p in reviews]
        except:
            raise Exception("Invalid reviews list, it must be iterable and contain only integers.")

    def __str__(self):
        return f'post_id={self.post_id}, author={self.author}, '\
               f'msg={self.msg}, reviews={self.reviews}'

    def __eq__(self, other):
        return isinstance(other, Post) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return isinstance(other, Post) and self.__dict__ != other.__dict__


post1 = Post(**post_data)
post2 = Post(**post_data)
print(post1)
print(post1 == post2, post1 is post2)
