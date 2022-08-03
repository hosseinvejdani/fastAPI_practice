from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()




# how to use path and query parameters at the same time in fastapi ------------------------------
@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {"message": f"blog id {id} comment id {comment_id} {valid=} {username=}"}


