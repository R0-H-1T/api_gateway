from fastapi import FastAPI, status
from .helper import Tags
from app.auth import auth
from app.qna import qna
from app.analytics import main

app = FastAPI(title="Api Gateway")


@app.get("/api/v1/health", tags=[Tags.home], status_code=status.HTTP_204_NO_CONTENT)
async def health():
    return


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
    responses={404: {"description": "Not Found"}},
)
