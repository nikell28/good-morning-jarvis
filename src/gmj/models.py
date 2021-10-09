import pydantic


class Question(pydantic.BaseModel):
    text: str = pydantic.Field(
        description='The text of the question you want to get an answer to')


class Answer(pydantic.BaseModel):
    text: str = pydantic.Field(
        description='The text of the answer to the question you asked')
