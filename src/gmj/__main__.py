import uvicorn

from gmj.config import settings


if __name__ == '__main__':
    uvicorn.run(
        app="gmj.app:app", host=settings.host, port=settings.port,
        reload=settings.debug)
