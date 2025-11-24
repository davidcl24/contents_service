"""
Genre schemas that map the JSON that comes from the request
or has to be sent back as a reply
"""
from sqlmodel import SQLModel


class GenreCreate(SQLModel):
    """Schema that contains the necessary data to create a new genre"""
    name: str

class GenreResponse(GenreCreate):
    """Schema that contains the genre data that should be returned to the client. It inherits the create schema"""
    id: int

class GenreUpdate(SQLModel):
    """Schema used to update an existing genre"""
    name: str | None