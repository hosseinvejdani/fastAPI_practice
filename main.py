from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()



# how to use path parameter + status code + response in fastapi ---------------------------------------------------
@app.get('/blog/{id}', status_code=status.HTTP_200_OK) # default status_code 
def get_blog(id: int, response:Response): 
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Error": f"Blog {id} Not Found !"}
    return {'message': f'blog {id}'}