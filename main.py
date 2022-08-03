from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()




# how to use query parameter in fastapi -------------------------------------------
@app.get('/blog')
def get_blog(id: int):
    return {"message": f"blog id is {id}"}

