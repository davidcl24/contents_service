from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from app.db.session import get_session
from app.models.genre import Genre
from app.schemas.genre import GenreCreate, GenreResponse, GenreUpdate


class GenreService:
    """It contains the CRUD for the genres table in the DB"""
    def __init__(self, session: Session = Depends(get_session)):
        """Instantiates an object of the GenreService class with a session to communicate with the DB"""
        self.session = session

    def create(self, genre_data: GenreCreate) -> GenreResponse:
        """Creates a new genre based on the received schema"""
        genre = Genre(**genre_data.model_dump())
        self.session.add(genre)
        self.session.commit()
        self.session.refresh(genre)
        return GenreResponse(**genre.model_dump())

    def get_all(self):
        """Returns a list of all existing genres"""
        query = select(Genre)
        return self.session.exec(query)

    def get_by_id(self, genre_id: int):
        """Returns only the desired genre"""
        return self.session.get(Genre, genre_id)

    def update(self, genre_id: int, genre_data: GenreUpdate) -> Genre:
        """Updates an existing genre based on the received schema"""
        genre = self.session.get(Genre, genre_id)
        if not genre:
            raise HTTPException(status_code=404, detail="Genre not found")

        genre_dict = genre_data.model_dump(exclude_unset=True)
        for key, value in genre_dict.items():
            setattr(genre, key, value)

        self.session.add(genre)
        self.session.commit()
        self.session.refresh(genre)
        return genre

    def delete(self, genre_id: int):
        """Removes the desired genre from the DB"""
        genre = self.session.get(Genre, genre_id)
        if not genre:
            raise HTTPException(status_code=404, detail="Genre not found")

        self.session.delete(genre)
        self.session.commit()
        return {"message": "Genre successfully deleted"}