from pydantic import (
    BaseSettings,
    PostgresDsn,
)


class Settings(BaseSettings):
    pg_dsn: PostgresDsn = 'postgresql+psycopg2://postgres:postgres@db:5432'

    class Config:
        env_file = '.env'
        
