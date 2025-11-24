from sqlmodel import SQLModel, Field


class MovieActorLink(SQLModel, table=True):
    """
    Represents the N:N relation between the movies and actors entities.
    """
    __tablename__ = "movies_actors"

    movies_id: int | None = Field(default=None, foreign_key="movies.id", primary_key=True)
    actors_id: int | None = Field(default=None, foreign_key="actors.id", primary_key=True)