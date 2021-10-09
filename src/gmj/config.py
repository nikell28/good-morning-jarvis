import pydantic

from gmj import __version__


class Settings(pydantic.BaseSettings):
    app_title: str = "Good Morning Jarvis"
    app_version: str = __version__
    app_description: str = (
        "A skill for Alice who wishes you a 'good morning' in a new way"
    )

    debug: bool = True

    host: str = "127.0.0.1"
    port: int = 8000
    http_timeout: float = 180.0

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
