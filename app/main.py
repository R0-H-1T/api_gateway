from fastapi import FastAPI
from .helper import Tags
from app.auth import auth
from app.qna import qna
from app.analytics import main

app = FastAPI(title="Api Gateway")


@app.get("/", tags=[Tags.home])
async def home():
    return {"data": "Welcome to  API Gateway"}


app.include_router(
    auth.router,
    prefix="/quiz-app/api/v1/auth",
    responses={404: {"description": "Not Found"}},
)


app.include_router(
    qna.router,
    prefix="/quiz-app/api/v1/qna",
    responses={404: {"description": "Not Found"}},
)


app.include_router(
    main.router,
    prefix="/quiz-app/api/v1/analytics",
    responses={404: {"description": "Not Found"}}
)