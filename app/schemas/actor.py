"""
Actor schemas that map the JSON that comes from the request
or has to be sent back as a reply
"""
from sqlmodel import SQLModel
from datetime import date


class ActorCreate(SQLModel):
    """Schema that contains the necessary data to create a new actor"""
    name: str
    birth: date | None = None

class ActorResponse(ActorCreate):
    """Schema that contains the actor data that should be returned to the client. It inherits the create schema"""
    id: int

class ActorUpdate(SQLModel):
    """Schema used to update an existing actor"""
    name: str | None = None
    birth: date | None = None