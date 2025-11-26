from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import sqlite3
import os
from datetime import datetime

# Database setup
DATABASE = "notice.db"

def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    if os.path.exists(DATABASE):
        return 
    with sqlite3.connect(DATABASE) as conn:
        with open('schema.sql', 'r') as f:
            conn.cursor().executescript(f.read())
        conn.commit()

app = FastAPI()

# Initialize database on startup
init_db()


# HTML 템플릿 파일이 있는 디렉토리 설정
templates = Jinja2Templates(directory="templates/")

# 정적 파일 (CSS, JS, 이미지 등)을 위한 디렉토리 설정 (예시)
# 만약 정적 파일이 없다면 이 부분은 생략 가능합니다.
# static_directory = "static" 
# if not os.path.exists(static_directory):
#     os.makedirs(static_directory)
# app.mount("/static", StaticFiles(directory=static_directory), name="static")

class NoticeSchema(BaseModel):
    title: str
    content: str

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

# Notice Board routes

# 1. 공지사항 목록 조회 (List)
@app.get("/notice", response_class=HTMLResponse)
async def notice_list(request: Request):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM notices ORDER BY created_at DESC")
    notices = cursor.fetchall()
    db.close()
    return templates.TemplateResponse("notice_list.html", {"request": request, "notices": notices})

# 2. 공지사항 생성 페이지 (Create Form)
@app.get("/notice/create", response_class=HTMLResponse)
async def notice_create_form(request: Request):
    return templates.TemplateResponse("notice_create.html", {"request": request})

# 3. 공지사항 신규 데이터 저장 (Create Action)
@app.post("/notice/create")
async def notice_create(request: Request, title: str = Form(...), content: str = Form(...)):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO notices (title, content, created_at, updated_at) VALUES (?, ?, ?, ?)",
                   (title, content, datetime.now(), datetime.now()))
    db.commit()
    db.close()
    return RedirectResponse(url="/notice", status_code=303)

# 4. 공지사항 상세 조회 (Read)
@app.get("/notice/{notice_id}", response_class=HTMLResponse)
async def notice_detail(request: Request, notice_id: int):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM notices WHERE id = ?", (notice_id,))
    notice = cursor.fetchone()
    db.close()
    return templates.TemplateResponse("notice_detail.html", {"request": request, "notice": notice})

# 5. 공지사항 수정 페이지 (Update Form)
@app.get("/notice/{notice_id}/edit", response_class=HTMLResponse)
async def notice_edit_form(request: Request, notice_id: int):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM notices WHERE id = ?", (notice_id,))
    notice = cursor.fetchone()
    db.close()
    return templates.TemplateResponse("notice_edit.html", {"request": request, "notice": notice})

# 6. 공지사항 수정 반영 (Update Action)
@app.post("/notice/{notice_id}/edit")
async def notice_edit(request: Request, notice_id: int, title: str = Form(...), content: str = Form(...)):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE notices SET title = ?, content = ?, updated_at = ? WHERE id = ?",
                   (title, content, datetime.now(), notice_id))
    db.commit()
    db.close()
    return RedirectResponse(url=f"/notice/{notice_id}", status_code=303)

# 7. 공지사항 삭제 (Delete)
@app.post("/notice/{notice_id}/delete")
async def notice_delete(notice_id: int):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM notices WHERE id = ?", (notice_id,))
    db.commit()
    db.close()
    return RedirectResponse(url="/notice", status_code=303)
