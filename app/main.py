from typing import Union
from fastapi import FastAPI
from app import routers

app = FastAPI()
app.include_router(routers.router)

# http://127.0.0.1:8000/api/v1/users/auth/login


# 여러 라우터 한번에 등록

    
@app.get("/")
def app_start():
    return {"Hello":"World"}

