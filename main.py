from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()



# How to use path parameter in fastapi -------------------------------------------
@app.get('/blog/{id}')
def get_blog(id: int):
    return {'message': f'blog id is {id}'}


