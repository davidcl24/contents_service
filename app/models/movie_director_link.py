from sqlmodel import SQLModel, Field


class MovieDirectorLink(SQLModel, table=True):
    __tablename__ = "movies_directors"

    movie_id: int | None = Field(default=None, foreign_key="movie.id", primary_key=True)
    director_id: int | None = Field(default=None, foreign_key="director.id", primary_key=True)