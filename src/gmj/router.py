from fastapi import APIRouter, Depends

from gmj.models import Answer, Question
from gmj.service import GoodMorningService
from gmj.depends import get_good_morning_service

router = APIRouter()


@router.put("/question/", response_model=Answer)
async def ask_question(
    question: Question, good_morning_service: GoodMorningService = Depends(
        get_good_morning_service)):
    """
    Ask a question
    """
    return await good_morning_service.give_answer(question)
