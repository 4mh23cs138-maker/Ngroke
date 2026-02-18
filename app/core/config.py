import os
from dotenv import load_dotenv

load_dotenv()


def get_database_url() -> str:
    # Vercel Postgres provides POSTGRES_URL. Fallback to local sqlite for quick start.
    url = os.getenv("POSTGRES_URL") or os.getenv("DATABASE_URL")
    if not url:
        return "sqlite:///./app.db"

    # SQLAlchemy expects postgresql+psycopg2://
    if url.startswith("postgres://"):
        return url.replace("postgres://", "postgresql+psycopg2://", 1)
    if url.startswith("postgresql://"):
        return url.replace("postgresql://", "postgresql+psycopg2://", 1)
    return url


DATABASE_URL = get_database_url()
