from datetime import date
from typing import Optional

from pydantic import field_validator
from sqlmodel import SQLModel

from app.models.genre import Genre
from app.schemas.director import DirectorResponse
from app.schemas.actor import ActorResponse

class ShowCreate(SQLModel):
    title: str
    synopsis: str | None = None
    seasons_num: int | None = None
    release_date: date | None = None
    genre_id: int | None = None
    poster_url: str | None = None
    rating: float | None = None
    is_published: bool | None = None
    directors_ids: list[int] | None = None
    actors_ids: list[int] | None = None

    @field_validator("rating", mode="before")
    @classmethod
    def parse_rating(cls, v):
        if v is None:
            return v
        return float(v)

class ShowResponse(ShowCreate):
    id: int

class ShowResponseExtended(ShowResponse):
    genre: Optional["Genre"]
    directors: list["DirectorResponse"]
    actors: list["ActorResponse"]

class ShowUpdate(SQLModel):
    title: str | None = None
    synopsis: str | None = None
    seasons_num: int | None = None
    release_date: date | None = None
    genre_id: int | None = None
    poster_url: str | None = None
    rating: float | None = None
    is_published: bool | None = None
    directors_ids: list[int] | None = None
    actors_ids: list[int] | None = None

    @field_validator("rating", mode="before")
    @classmethod
    def parse_rating(cls, v):
        if v is None:
            return v
        return float(v)