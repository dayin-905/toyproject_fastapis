from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# HTML 템플릿 파일이 있는 디렉토리 설정
templates = Jinja2Templates(directory="templates/")

# 정적 파일 (CSS, JS, 이미지 등)을 위한 디렉토리 설정 (예시)
# 만약 정적 파일이 없다면 이 부분은 생략 가능합니다.
# static_directory = "static" 
# if not os.path.exists(static_directory):
#     os.makedirs(static_directory)
# app.mount("/static", StaticFiles(directory=static_directory), name="static")

# http://127.0.0.1:8000/
@app.get("/")
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# http://127.0.0.1:8000/admin
@app.get("/admin")
async def read_admin(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

# http://127.0.0.1:8000/bakery
@app.get("/bakery")
async def read_bakery(request: Request):
    return templates.TemplateResponse("bakery.html", {"request": request})
