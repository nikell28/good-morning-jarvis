from gmj.models import Answer, Question


class GoodMorningService:
    async def give_answer(self, question: Question) -> Answer:
        return Answer(text=question.text)
