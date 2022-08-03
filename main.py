from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()



# How to use tags, summary and description in fastapi -------------------------------------------
@app.get('/blog/{id}',tags=['blog'],summary='Get blog by id', description='Get blog by id')
def get_blog(id: int):
    return {'message': f'blog id is {id}'}


