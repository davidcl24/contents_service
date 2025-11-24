from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from app.db.session import get_session
from app.models.actor import Actor
from app.models.director import Director
from app.models.movie import Movie
from app.schemas.movie import MovieCreate, MovieResponse, MovieUpdate


class MovieService:
    """It contains the CRUD for the movies table in the DB"""
    def __init__(self, session: Session = Depends(get_session)):
        """Instantiates an object of the MovieService class with a session to communicate with the DB"""
        self.session = session

    def create(self, movie_data: MovieCreate) -> MovieResponse:
        """Creates a new movie and its N:N relation with directors and actors based on the received schema"""
        movie = Movie(**movie_data.model_dump())

        if movie_data.directors_ids:
            statement = select(Director).where(Director.id.in_(movie_data.directors_ids))
            directors = list(self.session.exec(statement).all())
            movie.directors = directors

        if movie_data.actors_ids:
            statement = select(Actor).where(Actor.id.in_(movie_data.actors_ids))
            actors = list(self.session.exec(statement).all())
            movie.actors = actors

        self.session.add(movie)
        self.session.commit()
        self.session.refresh(movie)
        return MovieResponse(**movie.model_dump())

    def get_all(self):
        """Returns a list of all existing movies"""
        query = select(Movie)
        return self.session.exec(query).all()

    def get_by_id(self, movie_id: int):
        """Returns only the desired movie"""
        return self.session.get(Movie, movie_id)

    def get_by_genre(self, genre_id: int):
        """Returns a list of all movies in a genre"""
        statement = select(Movie).where(Movie.genre_id == genre_id)
        result = self.session.exec(statement)
        return result.all()

    def get_with_actor(self, actor_id: int):
        """Returns a list of all movies with an actor in it"""
        actor = self.session.get(Actor, actor_id)
        return actor.movies

    def get_with_director(self, director_id: int):
        """Returns a list of all movies with a director in it"""
        director = self.session.get(Director, director_id)
        return director.movies

    def get_batch(self, ids: list[int]):
        """Returns a list of the desired movies based on a list of IDs"""
        statement = select(Movie).where(Movie.id.in_(ids))
        results = self.session.exec(statement).all()

        if not results:
            raise HTTPException(status_code=404, detail="Movies not found")

        return results

    def update(self, movie_id: int, movie_data: MovieUpdate) -> Movie:
        """Updates an existing movie and its N:N relation with directors and actors based on the received schema"""
        movie = self.session.get(Movie, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")

        movie_dict = movie_data.model_dump(exclude_unset=True, exclude={"directors_ids", "actors_ids"})
        for key, value in movie_dict.items():
            setattr(movie, key, value)

        if movie_data.directors_ids:
            statement = select(Director).where(Director.id.in_(movie_data.directors_ids))
            directors = list(self.session.exec(statement).all())
            movie.directors = directors

        if movie_data.actors_ids:
            statement = select(Actor).where(Actor.id.in_(movie_data.actors_ids))
            actors = list(self.session.exec(statement).all())
            movie.actors = actors

        self.session.add(movie)
        self.session.commit()
        self.session.refresh(movie)
        return movie

    def delete(self, movie_id: int):
        """Removes the desired movie from the DB"""
        movie = self.session.get(Movie, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")

        self.session.delete(movie)
        self.session.commit()
        return {"message": "Movie successfully deleted"}
