"""
It contains all of the endpoints directly related to genres
"""

from fastapi import APIRouter, Depends

from app.schemas.genre import GenreResponse, GenreCreate, GenreUpdate
from app.services.genre_service import GenreService

router = APIRouter(tags=["Genres"])

@router.post("/genres", response_model=GenreResponse)
async def create_genre(genre: GenreCreate, service: GenreService = Depends()):
    """Handles the specific POST HTTP request to create a new genre and returns the created genre as JSON if successful"""
    return service.create(genre)

@router.get("/genres", response_model=list[GenreResponse])
async def read_genres(service: GenreService = Depends()):
    """Handles the specific GET HTTP request and returns a list of all existing genres as JSON"""
    return service.get_all()

@router.get("/genres/{genre_id}", response_model=GenreResponse)
async def read_genre(genre_id: int, service: GenreService = Depends()):
    """Handles the specific GET HTTP request and returns a specific genre as JSON"""
    return service.get_by_id(genre_id)

@router.patch("/genres/{genre_id}", response_model=GenreResponse)
async def update_genre(genre_id: int, genre_data: GenreUpdate, service: GenreService = Depends()):
    """Handles the specific PATCH HTTP request to update an existing genre and returns the updated genre as JSON if successful"""
    return service.update(genre_id, genre_data)

@router.delete("/genres/{genre_id}", response_model=dict)
async def delete_genre(genre_id: int, service: GenreService = Depends()):
    """Handles the specific DELETE HTTP request to delete an existing actor and returns a dict as JSON if successful"""
    return service.delete(genre_id)