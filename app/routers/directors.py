"""
It contains all of the endpoints directly related to directors
"""

from fastapi import APIRouter, Depends

from app.schemas.director import DirectorResponse, DirectorCreate, DirectorUpdate
from app.services.director_service import DirectorService

router = APIRouter(tags=["Directors"])

@router.post("/directors", response_model=DirectorResponse)
async def create_director(director: DirectorCreate, service: DirectorService = Depends()):
    """Handles the specific POST HTTP request to create a new director and returns the created director as JSON if successful"""
    return service.create(director)

@router.get("/directors", response_model=list[DirectorResponse])
async def read_directors(service: DirectorService = Depends()):
    """Handles the specific GET HTTP request and returns a list of all existing directors as JSON"""
    return service.get_all()

@router.get("/directors/{director_id}", response_model=DirectorResponse)
async def read_director(director_id: int, service: DirectorService = Depends()):
    """Handles the specific GET HTTP request and returns a specific director as JSON"""
    return service.get_by_id(director_id)

@router.get("/movies/{movie_id}/directors", response_model=list[DirectorResponse])
async def read_directors_from_movie(movie_id: int, service: DirectorService = Depends()):
    """Handles the specific GET HTTP request and returns a list of all directors in a specific movie as JSON"""
    return service.get_from_movie(movie_id)

@router.get("/shows/{show_id}/directors", response_model=list[DirectorResponse])
async def read_directors_from_show(show_id: int, service: DirectorService = Depends()):
    """Handles the specific GET HTTP request and returns a list of all directors in a specific show as JSON"""
    return service.get_from_show(show_id)

@router.patch("/directors/{director_id}", response_model=DirectorResponse)
async def update_director(director_id: int, director_data: DirectorUpdate, service: DirectorService = Depends()):
    """Handles the specific PATCH HTTP request to update an existing director and returns the updated director as JSON if successful"""
    return service.update(director_id, director_data)

@router.delete("/directors/{director_id}", response_model=dict)
async def delete_director(director_id: int, service: DirectorService = Depends()):
    """Handles the specific DELETE HTTP request to delete an existing director and returns a dict as JSON if successful"""
    return service.delete(director_id)