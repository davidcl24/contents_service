from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from app.db.session import get_session
from app.models.actor import Actor
from app.models.movie import Movie
from app.models.show import Show
from app.schemas.actor import ActorCreate, ActorResponse, ActorUpdate


class ActorService:
    """It contains the CRUD for the actors table in the DB"""
    def __init__(self, session: Session = Depends(get_session)):
        """Instantiates an object of the ActorService class with a session to communicate with the DB"""
        self.session = session

    def create(self, actor_data: ActorCreate) -> ActorResponse:
        """Creates a new actor based on the received schema"""
        actor = Actor(**actor_data.model_dump())
        self.session.add(actor)
        self.session.commit()
        self.session.refresh(actor)
        return ActorResponse(**actor.model_dump())

    def get_all(self):
        """Returns a list of all existing actors"""
        query = select(Actor)
        return self.session.exec(query).all()

    def get_by_id(self, actor_id: int):
        """Returns only the desired actor"""
        return self.session.get(Actor, actor_id)

    def get_from_movie(self, movie_id: int):
        """Returns a list of all actors in a movie"""
        movie = self.session.get(Movie, movie_id)
        return movie.actors

    def get_from_show(self, show_id: int):
        """Returns a list of all actors in a show"""
        show = self.session.get(Show, show_id)
        return show.actors

    def update(self, actor_id: int, actor_data: ActorUpdate) -> Actor:
        """Updates an existing actor based on the received schema"""
        actor = self.session.get(Actor, actor_id)
        if not actor:
            raise HTTPException(status_code=404, detail="Actor not found")

        actor_dict = actor_data.model_dump(exclude_unset=True)
        for key, value in actor_dict.items():
            setattr(actor, key, value)

        self.session.add(actor)
        self.session.commit()
        self.session.refresh(actor)
        return actor

    def delete(self, actor_id: int):
        """Removes the desired actor from the DB"""
        actor = self.session.get(Actor, actor_id)
        if not actor:
            raise HTTPException(status_code=404, detail="Actor not found")

        self.session.delete(actor)
        self.session.commit()
        return {"message": "Actor successfully deleted"}