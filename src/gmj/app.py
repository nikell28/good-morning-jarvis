from fastapi import FastAPI

from gmj.config import settings
from gmj.router import router

app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
    version=settings.app_version,
    openapi_tags=[
        {
            "name": "gmj",
            "description": "Answers to Alice's questions",
        }
    ],
    debug=settings.debug
)

app.include_router(router, prefix="")
