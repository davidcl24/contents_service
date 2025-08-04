from datetime import date

from sqlmodel import SQLModel, Relationship, Field

from app.models.movie_director_link import MovieDirectorLink
from app.models.show_director_link import ShowDirectorLink


class Director(SQLModel, table=True):
    __tablename__ = "directors"

    id: int | None=Field(default=None, primary_key=True)
    name: str | None
    birth: date | None

    shows: list["Show"] = Relationship(back_populates="directors", link_model=ShowDirectorLink)
    movies: list["Movie"] = Relationship(back_populates="directors", link_model=MovieDirectorLink)