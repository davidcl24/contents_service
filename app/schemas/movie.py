from datetime import date

from pydantic import field_validator
from sqlmodel import SQLModel


class MovieCreate(SQLModel):
    title: str
    synopsis: str | None = None
    length: int | None = None
    release_date: date | None = None
    genre_id: int | None = None
    poster_url: str | None = None
    rating: float | None = None
    is_published: bool | None = None
    file_key: str | None = None  # Delete the None in production

    @field_validator("rating", mode="before")
    @classmethod
    def parse_rating(cls, v):
        if v is None:
            return v
        return float(v)


class MovieResponse(MovieCreate):
    id: int

class MovieUpdate(SQLModel):
    title: str | None = None
    synopsis: str | None = None
    length: int | None = None
    release_date: date | None = None
    genre_id: int | None = None
    poster_url: str | None = None
    rating: float | None = None
    is_published: bool | None = None
    file_key: str | None = None # Delete the None in production

    @field_validator("rating", mode="before")
    @classmethod
    def parse_rating(cls, v):
        if v is None:
            return v
        return float(v)