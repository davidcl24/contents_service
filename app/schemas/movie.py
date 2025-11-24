"""
Movie schemas that map the JSON that comes from the request
or has to be sent back as a reply
"""
from datetime import date
from typing import Optional

from pydantic import field_validator
from sqlmodel import SQLModel

from app.models.genre import Genre
from app.schemas.director import DirectorResponse
from app.schemas.actor import ActorResponse


class MovieCreate(SQLModel):
    """Schema that contains the necessary data to create a new movie"""
    title: str
    synopsis: str | None = None
    length: int | None = None
    release_date: date | None = None
    genre_id: int | None = None
    poster_url: str | None = None
    rating: float | None = None
    is_published: bool | None = None
    file_key: str | None = None  # Delete the None in production
    directors_ids: list[int] | None = None
    actors_ids: list[int] | None = None

    @field_validator("rating", mode="before")
    @classmethod
    def parse_rating(cls, v):
        """Safely parses the data that comes in JSON in the rating field to float when creating a new movie"""
        if v is None:
            return v
        return float(v)


class MovieResponse(MovieCreate):
    """Schema that contains the movie data that should be returned to the client. It inherits the create schema"""
    id: int

class MovieResponseExtended(MovieResponse):
    """Schema that contains the same data as the other response schema but with extra stuff.
    It inherits the base MovieResponse schema"""
    genre: Optional["Genre"]
    directors: list["DirectorResponse"]
    actors: list["ActorResponse"]

class MovieUpdate(SQLModel):
    """Schema used to update an existing movie"""
    title: str | None = None
    synopsis: str | None = None
    length: int | None = None
    release_date: date | None = None
    genre_id: int | None = None
    poster_url: str | None = None
    rating: float | None = None
    is_published: bool | None = None
    file_key: str | None = None # Delete the None in production
    directors_ids: list[int] | None = None
    actors_ids: list[int] | None = None

    @field_validator("rating", mode="before")
    @classmethod
    def parse_rating(cls, v):
        """Safely parses the data that comes in JSON in the rating field to float when updating an existing movie"""
        if v is None:
            return v
        return float(v)