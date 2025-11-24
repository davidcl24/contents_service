from datetime import date

from sqlmodel import SQLModel, Field, Relationship

from app.models.movie_actor_link import MovieActorLink
from app.models.show_actor_link import ShowActorLink


class Actor(SQLModel, table=True):
    """
    Represents the `actors` entity in the database and its relations
    with other entities.
    """
    __tablename__ = "actors"

    id: int | None=Field(default=None, primary_key=True)
    name: str | None
    birth: date | None

    shows: list["Show"] = Relationship(back_populates="actors", link_model=ShowActorLink)
    movies: list["Movie"] = Relationship(back_populates="actors", link_model=MovieActorLink)