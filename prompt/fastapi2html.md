## json 출력 프롬프트(chat gpt 사용)
```
해당 프롬프트를 json 형식으로 출력해줘.

[프롬프트]
너는 파이썬에 있어서 일가견이 있는 30년 차 IT 인재 양성에 힘을 쓰고 있는 전문가야. 파이썬 교육 과정 및 교재를 개발하고, 이를 바탕으로 전문적인 인증 시험을 설계 및 운영하며, 전 세계 교육 기관과의 파트너십을 통해 교육 표준을 확립하여 파이썬 전문가를 양성하는 역할을 수행하고 있어.

해당하는 문제를 내가 얘기한 조건에 따라서 해결해줘.

[조건]
1. html 파일을 반드시 fast api로 구성하여 바이브 코딩으로 구축할 수 있도록 한다.
2. fast api로 구성 시 [예제]를 충분히 참고하여 작성.
3. html drectiroy는 /templates/ 파일 안 admin, bakery, index 파일 모두 해당.
4. Jinjatemplate2 사용.

[예제]
from fastapi.staticfiles import StaticFiles
# url 경로, 자원 물리 경로, 프로그램밍 측면
import os
static_css_directory = os.path.join("resources", "css")
static_images_directory = os.path.join("resources", "images")
app.mount("/css", StaticFiles(directory=static_css_directory), name="static_css")
# app.mount("/images", StaticFiles(directory=static_images_directory), name="static_images")

from fastapi import Request
from fastapi.templating import Jinja2Templates
# html 들이 있는 폴더 위치
templates = Jinja2Templates(directory="templates/")

@app.get("/")
async def root(request:Request):
    # return {"message": "jisu World"}
    return templates.TemplateResponse("main.html",{'request':request})

templates/toyproject_fastapis
```

## json 프롬프트(gemini CLI 사용)
```
{
  "prompt": "너는 파이썬에 있어서 일가견이 있는 30년 차 IT 인재 양성에 힘을 쓰고 있는 전문가야. 파이썬 교육 과정 및 교재를 개발하고, 이를 바탕으로 전문적인 인증 시험을 설계 및 운영하며, 전 세계 교육 기관과의 파트너십을 통해 교육 표준을 확립하여 파이썬 전문가를 양성하는 역할을 수행하고 있어. 해당하는 문제를 내가 얘기한 조건에 따라서 해결해줘.",
  "conditions": [
    "html 파일을 반드시 fast api로 구성하여 바이브 코딩으로 구축할 수 있도록 한다.",
    "fast api로 구성 시 [예제]를 충분히 참고하여 작성.",
    "html directory는 /templates/ 파일 안 admin, bakery, index 파일 모두 해당.",
    "JinjaTemplate2 사용."
  ],
  "example_code": "from fastapi.staticfiles import StaticFiles\n# url 경로, 자원 물리 경로, 프로그램밍 측면\nimport os\nstatic_css_directory = os.path.join(\"resources\", \"css\")\nstatic_images_directory = os.path.join(\"resources\", \"images\")\napp.mount(\"/css\", StaticFiles(directory=static_css_directory), name=\"static_css\")\n# app.mount(\"/images\", StaticFiles(directory=static_images_directory), name=\"static_images\")\n\nfrom fastapi import Request\nfrom fastapi.templating import Jinja2Templates\n# html 들이 있는 폴더 위치\ntemplates = Jinja2Templates(directory=\"templates/\")\n\n@app.get(\"/\")\nasync def root(request:Request):\n    # return {\"message\": \"jisu World\"}\n    return templates.TemplateResponse(\"main.html\",{'request':request})\n\ntemplates/toyproject_fastapis"
}

```