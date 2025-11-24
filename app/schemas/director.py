"""
Director schemas that map the JSON that comes from the request
or has to be sent back as a reply
"""
from sqlmodel import SQLModel
from datetime import date


class DirectorCreate(SQLModel):
    """Schema that contains the necessary data to create a new director"""
    name: str
    birth: date | None = None

class DirectorResponse(DirectorCreate):
    """Schema that contains the director data that should be returned to the client. It inherits the create schema"""
    id: int

class DirectorUpdate(SQLModel):
    """Schema used to update an existing director"""
    name: str | None = None
    birth: date | None = None