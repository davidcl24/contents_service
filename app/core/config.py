from pydantic_settings import BaseSettings

class Config(BaseSettings):
    db_host: str = "localhost"
    db_port: str = "5432"
    db_username: str = "default"
    db_password: str = "example"
    db_database: str = "streamingdb"

    class Config:
        env_file = ".env"

config = Config()