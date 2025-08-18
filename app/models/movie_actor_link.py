from sqlmodel import SQLModel, Field


class MovieActorLink(SQLModel, table=True):
    __tablename__ = "movies_actors"

    movies_id: int | None = Field(default=None, foreign_key="movies.id", primary_key=True)
    actors_id: int | None = Field(default=None, foreign_key="actors.id", primary_key=True)