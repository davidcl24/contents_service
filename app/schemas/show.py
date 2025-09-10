from datetime import date

from sqlmodel import SQLModel


class ShowCreate(SQLModel):
    title: str
    synopsis: str | None = None
    seasons_num: int | None = None
    release_date: date | None = None
    genre_id: int | None = None
    poster_url: str | None = None
    rating: float | None = None
    is_published: bool | None = None

class ShowResponse(ShowCreate):
    id: int

class ShowUpdate(SQLModel):
    title: str | None = None
    synopsis: str | None = None
    seasons_num: int | None = None
    release_date: date | None = None
    genre_id: int | None = None
    poster_url: str | None = None
    rating: float | None = None
    is_published: bool | None = None