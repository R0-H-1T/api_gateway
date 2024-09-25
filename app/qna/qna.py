from fastapi import APIRouter
from ..helper import Tags

router = APIRouter(tags=[Tags.qna])


@router.post("/question")
async def question():
    return {"data": "question"}


@router.post("/answer")
async def answer():
    return {"data": "answer"}


@router.get("/questionnaire/{qna_id}")
async def get_qna(qna_id: int):
    pass
