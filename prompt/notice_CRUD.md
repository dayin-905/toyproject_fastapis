## 프롬프트 작성 주의사항 및 
- 예시로 준 DB 자료를 추가하지 못했음..
- 

## json 출력 작성 프롬프트(Chat gpt 사용)
```
너는 기업 고객을 대상으로 비즈니스 목표 달성을 위한 맞춤형 AI 전략 및 프롬프트 관리 시스템을 구축, 프롬프트 엔지니어링의 기술 원칙을 정립하고, 학습 가이드와 최신 연구를 공유하여 지식을 확산, 이미지 생성 AI 등을 활용하여 예술적이고 창의적인 고품질의 결과물을 만들어내는 데 특화되어 있는 AI 프롬프트 전문가야. 해당하는 html에 공지사항 리스트 게시판을 만들거야. 

공지사항 리스트 게시판에 사용할 기술은 CRUD가 구동될 수 있으면 돼. 오른쪽 상단에 notice이라는 버튼을 눌렀을 때 notice 게시판의 crud가 구동될 수 있는 아주 구체적인 프롬프트를 작성해줘.

프롬프트에 꼭 들어갈 내용
1. table을 만들 수 있게 sql을 작성
2. notic 게시판에 crud 구동
3. 필요에 따라 기존 html 수정가능하다는 문구 제시.
4. 디자인에 매우 신경쓰도록 함.
5. 프롬프트는 반드시 json 형식으로 출력
6. html 대상 : templates의 admin.html, bakery.html, index.html
```

## json 프롬프트
```
{
  "role": "AI Prompt Engineer",
  "goal": "HTML 기반 공지사항 리스트 게시판을 구축하며, 우측 상단 notice 버튼 클릭 시 CRUD 기능이 동작하도록 FastAPI 기반 상세 프롬프트 제작.",
  "html_targets": [
    "templates/admin.html",
    "templates/bakery.html",
    "templates/index.html"
  ],
  "instructions": {
    "overview": "당신은 기업 고객 대상 맞춤형 AI 전략·프롬프트 엔지니어링 전문 전문가이다. 아래 요구사항을 기반으로 공지사항(notice) 게시판의 UI, SQL, CRUD, FastAPI 라우팅, 템플릿 반영 등을 모두 포함하는 고도화된 프롬프트를 작성한다.",
    "requirements": [
      "SQL 테이블 생성 스키마 포함",
      "공지사항 게시판 CRUD 기능 구현",
      "기존 HTML(admin, bakery, index)은 필요 시 자유롭게 수정 가능하다는 문구 필수 포함",
      "디자인 퀄리티 최상급 기준으로 스타일 가이드 포함",
      "전체 프롬프트는 JSON 형태로 출력"
    ]
  },
  "prompt": {
    "task_description": "FastAPI + Jinja2 + HTML 기반 공지사항 리스트 게시판을 구현한다. 모든 HTML 템플릿(admin.html, bakery.html, index.html)에 우측 상단에 'notice' 버튼을 추가한다. 버튼 클릭 시 notice 목록 페이지로 이동하며, 목록·상세·등록·수정·삭제의 CRUD 기능이 모두 동작해야 한다. 필요하다면 templates 폴더의 admin.html, bakery.html, index.html은 자유롭게 수정해도 된다는 문구를 반드시 포함한다. 디자인은 기업 수준의 modern UI/UX로 고급스럽고 직관적인 형태로 구성한다.",
    "sql_schema": "CREATE TABLE notices (\n    id INTEGER PRIMARY KEY AUTOINCREMENT,\n    title TEXT NOT NULL,\n    content TEXT NOT NULL,\n    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\n    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n);",
    "fastapi_crud": {
      "routes": [
        { "method": "GET", "path": "/notice", "description": "공지사항 목록 조회", "template": "notice_list.html" },
        { "method": "GET", "path": "/notice/{notice_id}", "description": "공지사항 상세 조회", "template": "notice_detail.html" },
        { "method": "GET", "path": "/notice/create", "description": "공지사항 생성 페이지", "template": "notice_create.html" },
        { "method": "POST", "path": "/notice/create", "description": "공지사항 신규 데이터 저장" },
        { "method": "GET", "path": "/notice/{notice_id}/edit", "description": "공지사항 수정 페이지", "template": "notice_edit.html" },
        { "method": "POST", "path": "/notice/{notice_id}/edit", "description": "공지사항 수정 반영" },
        { "method": "POST", "path": "/notice/{notice_id}/delete", "description": "공지사항 삭제" }
      ],
      "database_layer": "SQLite 또는 PostgreSQL 기반. ORM(SQLAlchemy) 또는 sqlite3 사용 가능.",
      "jinja_templates": [
        "notice_list.html",
        "notice_detail.html",
        "notice_create.html",
        "notice_edit.html"
      ]
    },
    "ui_ux_guidelines": {
      "modern_design": [
        "상단 notice 버튼은 primary color(블루 계열)로 고정 배치",
        "notice_list.html은 카드형 또는 테이블형 UI 사용",
        "Hover shadow, border-radius 10~14px 적용한 고급형 스타일",
        "모바일 및 데스크톱 반응형 UI 구조",
        "공지 작성·수정 폼은 floating label 이벤트와 subtle animation 적용"
      ],
      "visual_requirements": "전체 디자인은 기업형 대시보드 느낌으로 구성하며, 컬러 팔레트는 블루·화이트·다크그레이 조합 유지."
    },
    "html_requirements": {
      "modifiable_statement": "templates/admin.html, templates/bakery.html, templates/index.html 파일은 notice 시스템 구현을 위해 자유롭게 수정 가능하다.",
      "components": [
        "각 HTML 파일의 우측 상단에 notice 이동 버튼 추가",
        "notice_list.html에서 CRUD 버튼 직관적 배치",
        "form 요소는 label, placeholder, validation 문구 포함"
      ]
    }
  }
}
```