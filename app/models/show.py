from datetime import date
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from app.models.genre import Genre
from app.models.show_actor_link import ShowActorLink
from app.models.show_director_link import ShowDirectorLink


class Show(SQLModel, table=True):
    __tablename__ = "shows"

    id: int | None = Field(default=None, primary_key=True)
    title: str | None = None
    synopsis: str | None = None
    seasons_num: int | None = None
    release_date: date | None = None
    genre_id: int | None = Field(default=None, foreign_key="genres.id")
    poster_url: str | None = None
    rating: int | None = None
    created_at: date | None = None
    updated_at: date | None = None
    is_published: bool | None = None

    genre: Optional[Genre] = Relationship(back_populates="shows")
    episodes: list["Episode"] = Relationship(back_populates="show")
    actors: list["Actor"] = Relationship(back_populates="shows", link_model=ShowActorLink)
    directors: list["Director"] = Relationship(back_populates="shows", link_model=ShowDirectorLink)