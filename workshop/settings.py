from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    DATABASE_URL: str = 'postgresql: // fastapi_basic_project: fastapi_user @ db:5432 / fastapi_basic_project'


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)