from typing import Annotated
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.helper import Tags
from app.dependency import get_async_client
from app.quiz_models.qna_models import Questionaire, Answers
from httpx import AsyncClient
import os
from dotenv import load_dotenv

router = APIRouter(tags=[Tags.qna])

load_dotenv()
prefix_url = f"http://{os.environ.get('QNA_DNS')}" or f"http://localhost:{os.getenv('QNA_PORT')}"


@router.post("/question", status_code=status.HTTP_201_CREATED)
async def question(
    questionnaire: Questionaire,
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())],
    client: Annotated[AsyncClient, Depends(get_async_client)],
):
    res = await client.post(
        url=f"{prefix_url}/question",
        headers={"Authorization": f"{credentials.scheme} {credentials.credentials}"},
        json=questionnaire.model_dump(),
    )

    if res.status_code != status.HTTP_201_CREATED:
        raise HTTPException(status_code=res.status_code)


@router.post("/answer", status_code=status.HTTP_201_CREATED)
async def answer(
    answer: Answers,
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())],
    client: Annotated[AsyncClient, Depends(get_async_client)],
):
    res = await client.post(
        url=f"{prefix_url}/answer",
        headers={"Authorization": f"{credentials.scheme} {credentials.credentials}"},
        json=answer.model_dump(),
    )

    if res.status_code != status.HTTP_201_CREATED:
        raise HTTPException(status_code=res.status_code)


@router.get("/questionnaire/{qna_id}", status_code=status.HTTP_200_OK)
async def get_qna(
    qna_id: int,
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())],
    client: Annotated[AsyncClient, Depends(get_async_client)],
):
    res = await client.get(
        url=f"{prefix_url}/get_qna/{qna_id}",
        headers={"Authorization": f"{credentials.scheme} {credentials.credentials}"},
    )

    return res.json()
