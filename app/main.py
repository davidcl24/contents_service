from fastapi import FastAPI
from sqlmodel import SQLModel

from app.db.session import engine
from app.routers import actors, directors, episodes, genres, movies, shows

app = FastAPI()


app.include_router(actors.router, prefix="/api")
app.include_router(directors.router, prefix="/api")
app.include_router(episodes.router, prefix="/api")
app.include_router(genres.router, prefix="/api")
app.include_router(movies.router, prefix="/api")
app.include_router(shows.router, prefix="/api")

def init_db():
    SQLModel.metadata.create_all(engine)

init_db()