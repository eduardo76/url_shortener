import os
from dotenv import load_dotenv

from pydantic import (
    BaseSettings,
    PostgresDsn,
)


load_dotenv()


class Settings(BaseSettings):
    pg_dsn: PostgresDsn = 'postgresql+psycopg2://postgres:postgres@db:5432'
    # pg_dsn: PostgresDsn = str(os.getenv('DATABASE_URL'))
 