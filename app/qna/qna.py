from typing import Annotated
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.helper import Tags
from app.dependency import get_async_client
from app.quiz_models.qna_models import Questionaire, Answers
from httpx import AsyncClient
import os
from dotenv import load_dotenv
import json

router = APIRouter(tags=[Tags.qna])
load_dotenv()
prefix_url = f"http://{os.environ.get('QNA_DNS')}" \
    if os.getenv('QNA_DNS') else f"http://localhost:{os.getenv('QNA_PORT')}"


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


@router.get("/all-questions", status_code=status.HTTP_200_OK)
async def get_questionnaires(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())],
    client: Annotated[AsyncClient, Depends(get_async_client)],
):
    print('reached')
    res = await client.get(
        url=f'{prefix_url}/all-questions',
        headers={'Authorization': f'{credentials.scheme} {credentials.credentials}'}
    )

    if res.status_code != status.HTTP_200_OK:
        raise HTTPException(res.status_code)
    return res.json()


@router.get("/quiz_result/{id}", status_code=status.HTTP_200_OK)
async def quiz_result(
    id: str,
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())],
    client: Annotated[AsyncClient, Depends(get_async_client)],
):
    res = await client.get(
        url=f'{prefix_url}/quiz_result/{id}',
        headers={'Authorization': f'{credentials.scheme} {credentials.credentials}'}
    )
    
    if res.status_code != status.HTTP_200_OK:
        raise HTTPException(res.status_code)
    
    return res.json()


@router.get("/quiz_code/{quiz_code}", status_code=status.HTTP_200_OK)
async def get_question_id(
    quiz_code: str,
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())],
    client: Annotated[AsyncClient, Depends(get_async_client)],
):
    res = await client.get(
        url=f'{prefix_url}/quiz_code/{quiz_code}',
        headers={'Authorization': f'{credentials.scheme} {credentials.credentials}'}
    )
    print('QUIZ_CODE')
    if res.status_code != status.HTTP_200_OK:
        raise HTTPException(res.status_code)
    return res.json()


@router.get("/question", status_code=status.HTTP_200_OK)
async def get_answer(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())],
    client: Annotated[AsyncClient, Depends(get_async_client)],
):
    res = await client.get(
        url=f'{prefix_url}/question',
        headers={'Authorization': f'{credentials.scheme} {credentials.credentials}'}
    )
    
    if res.status_code != status.HTTP_200_OK:
        raise HTTPException(res.status_code)
    
    return res.json()    


@router.get('/question/{id}', status_code=status.HTTP_200_OK)
async def get_quiz(
    id: str,
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())],
    client: Annotated[AsyncClient, Depends(get_async_client)]
):
    res = await client.get(
        url=f'{prefix_url}/question/{id}',
        headers={'Authorization': f'{credentials.scheme} {credentials.credentials}'}
    )

    if res.status_code != status.HTTP_200_OK:
        raise HTTPException(res.status_code)
    
    return res.json()


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


@router.delete("/question/{id}")
async def delete_quiz(
    id: str,
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())],
    client: Annotated[AsyncClient, Depends(get_async_client)]
):
    res = await client.delete(
        url=f"{prefix_url}/question/{id}",
        headers={"Authorization": f"{credentials.scheme} {credentials.credentials}"},
    )

    if res.status_code != status.HTTP_204_NO_CONTENT:
        raise HTTPException(
            status_code=res.status_code
        )
    