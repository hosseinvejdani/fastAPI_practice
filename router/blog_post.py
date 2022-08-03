from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

'''
this file shows you how to use post method and base model
'''

router = APIRouter(prefix='/blog', tags=['blog'])


class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]


@router.post('/new')
def create_blog(blog: BlogModel):
    return {"message": 'OK', "data": blog}