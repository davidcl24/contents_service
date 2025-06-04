from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from app.db.session import get_session
from app.models.genre import Genre
from app.schemas.genre import GenreCreate, GenreResponse, GenreUpdate


class GenreService:
    def __init__(self, session: Session = Depends(get_session())):
        self.session = session

    def create(self, genre_data: GenreCreate) -> GenreResponse:
        genre = Genre(**genre_data.model_dump())
        self.session.add(genre)
        self.session.commit()
        self.session.refresh(genre)
        return GenreResponse(**genre.model_dump())

    def get_all(self):
        query = select(Genre)
        return self.session.exec(query)

    def get_by_id(self, genre_id: int):
        return self.session.get(Genre, genre_id)

    def update(self, genre_id: int, genre_data: GenreUpdate) -> Genre:
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
        genre = self.session.get(Genre, genre_id)
        if not genre:
            raise HTTPException(status_code=404, detail="Genre not found")

        self.session.delete(genre)
        self.session.commit()
        return {"message": "Genre successfully deleted"}