from sqlmodel import SQLModel, Field, Relationship


class Genre(SQLModel, table=True):
    """
    Represents the `genres` entity in the database and its relations
    with other entities.
    """
    __tablename__ = "genres"

    id: int | None = Field(default=None, primary_key=True)
    name: str | None = None

    shows: list["Show"] = Relationship(back_populates="genre")
    movies: list["Movie"] = Relationship(back_populates="genre")