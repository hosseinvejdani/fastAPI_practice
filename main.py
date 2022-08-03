from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()



# How to use path parameter in fastapi -------------------------------------------
@app.get('/blog/{id}')
def get_blog(id: int):
    return {'message': f'blog id is {id}'}


# how to use query parameter in fastapi -------------------------------------------
@app.get('/blog')
def get_blog(id: int):
    return {"message": f"blog id is {id}"}

# How to use enum in fastapi -------------------------------------------
class TypeBlogs(str, Enum):
    Type1 = 'technology'
    Type2 = 'science'
    Type3 = 'medical'

@app.get('/blog/type/{type}')
def get_type_blog(type: TypeBlogs):
    return {'message': f'blog type is {type}'}



# how to use path and query parameters at the same time in fastapi ------------------------------
@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {"message": f"blog id {id} comment id {comment_id} {valid=} {username=}"}


# how to use optinal query parameters in fastapi ---------------------------------------------------
@app.get('/blog/all')
def get_blogs(page: Optional[int] = None, page_size: str = None):
    return {"message": f"{page=} -- {page_size=}"}



# how to use path parameter + status code + response in fastapi ---------------------------------------------------
@app.get('/blog/{id}', status_code=status.HTTP_200_OK) # default status_code 
def get_blog(id: int, response:Response): 
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Error": f"Blog {id} Not Found !"}
    return {'message': f'blog {id}'}