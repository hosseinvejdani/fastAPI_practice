from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()






# how to use optinal query parameters in fastapi ---------------------------------------------------
@app.get('/blog/all')
def get_blogs(page: Optional[int] = None, page_size: str = None):
    return {"message": f"{page=} -- {page_size=}"}


