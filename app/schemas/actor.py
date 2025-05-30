from sqlmodel import SQLModel


class ActorCreate(SQLModel):
    name: str
    birth: str | None = None

class ActorResponse(ActorCreate):
    id: int

class ActorUpdate(SQLModel):
    name: str | None = None
    birth: str | None = None