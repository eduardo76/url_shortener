import os
from pydantic import (
    BaseSettings,
    PostgresDsn,
    Field
)


class Settings(BaseSettings):
    BASE_URL: str = Field(..., env='BASE_URL')
    pg_dsn: str = Field(..., env='DATABASE_URL')

    class Config:
        env_file = '.env'
 