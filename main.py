from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()




# How to use enum in fastapi -------------------------------------------
class TypeBlogs(str, Enum):
    Type1 = 'technology'
    Type2 = 'science'
    Type3 = 'medical'

@app.get('/blog/type/{type}')
def get_type_blog(type: TypeBlogs):
    return {'message': f'blog type is {type}'}


