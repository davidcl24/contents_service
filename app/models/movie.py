from datetime import date
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship

from app.models.genre import Genre


class Movie(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str | None
    synopsis: str | None
    length: int | None
    release_date: date | None
    genre_id: int | None = Field(default=None, foreign_key="genre.id")
    poster_url: str | None
    rating: int | None
    created_at: date | None
    updated_at: date | None
    is_published: bool | None

    genre: Optional[Genre] = Relationship(back_populates="movies")