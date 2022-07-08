import sys

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from FallenRobot import DB_URL, LOGGER


if DB_URI and DB_URI.startswith("postgres://"):
    DB_URI = DB_URI.replace("postgres://", "postgresql://", 1)


def start() -> scoped_session:
    engine = create_engine(DB_URL, client_encoding="utf8")
    LOGGER.info("[PostgreSQL] Connecting to database......")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=True))


BASE = declarative_base()
try:
    SESSION: scoped_session = start()
except Exception as e:
    LOGGER.exception(f"[PostgreSQL] Failed to connect due to {e}")
    sys.exit()

LOGGER.info("[PostgreSQL] Connection successful, session started.")
