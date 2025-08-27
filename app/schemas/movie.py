from datetime import date

from sqlmodel import SQLModel


class MovieCreate(SQLModel):
    title: str
    synopsis: str | None = None
    length: int | None = None
    release_date: date | None = None
    genre_id: int | None = None
    poster_url: str | None = None
    rating: int | None = None
    is_published: bool | None = None
    file_key: str


class MovieResponse(MovieCreate):
    id: int

class MovieUpdate(SQLModel):
    title: str | None = None
    synopsis: str | None = None
    length: int | None = None
    release_date: date | None = None
    genre_id: int | None = None
    poster_url: str | None = None
    rating: int | None = None
    is_published: bool | None = None
    file_key: str