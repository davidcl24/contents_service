from sqlmodel import create_engine, Session
from app.core.config import config

engine = create_engine(
    "postgresql://" + config.db_username + ":" + config.db_password + "@" + config.db_host + ":" + config.db_port + "/" + config.db_database)


def get_session():
    with Session(engine) as session:
        yield session
