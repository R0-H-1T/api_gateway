from fastapi import FastAPI, status
from .helper import Tags
from app.auth import auth
from app.qna import qna
from app.analytics import main
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Api Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (Change to specific origin for security)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.get("/api/v1/health", tags=[Tags.home], status_code=status.HTTP_204_NO_CONTENT)
async def health():
    return


app.include_router(
    auth.router,
    prefix="/api/v1/auth",
    responses={404: {"description": "Not Found"}},
)


app.include_router(
    qna.router,
    prefix="/api/v1/qna",
    responses={404: {"description": "Not Found"}},
)


app.include_router(
    main.router,
    prefix="/api/v1/analytics",
    responses={404: {"description": "Not Found"}},
)
