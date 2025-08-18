from sqlmodel import SQLModel, Field


class MovieDirectorLink(SQLModel, table=True):
    __tablename__ = "movies_directors"

    movies_id: int | None = Field(default=None, foreign_key="movies.id", primary_key=True)
    directors_id: int | None = Field(default=None, foreign_key="directors.id", primary_key=True)