from fastapi import APIRouter, Depends

from app.schemas.director import DirectorResponse, DirectorCreate, DirectorUpdate
from app.services.director_service import DirectorService

router = APIRouter(tags=["Directors"])

@router.post("/directors", response_model=DirectorResponse)
async def create_director(director: DirectorCreate, service: DirectorService = Depends()):
    return service.create(director)

@router.get("/directors", response_model=list[DirectorResponse])
async def read_directors(service: DirectorService = Depends()):
    return service.get_all()

@router.get("/directors/{director_id}", response_model=DirectorResponse)
async def read_director(director_id: int, service: DirectorService = Depends()):
    return service.get_by_id(director_id)

@router.get("/movies/{movie_id}/directors", response_model=list[DirectorResponse])
async def read_directors_from_movie(movie_id: int, service: DirectorService = Depends()):
    return service.get_from_movie(movie_id)

@router.get("/shows/{show_id}/directors", response_model=list[DirectorResponse])
async def read_directors_from_show(show_id: int, service: DirectorService = Depends()):
    return service.get_from_show(show_id)

@router.patch("/directors/{director_id}", response_model=DirectorResponse)
async def update_director(director_id: int, director_data: DirectorUpdate, service: DirectorService = Depends()):
    return service.update(director_id, director_data)

@router.delete("/directors/{director_id}", response_model=dict)
async def delete_director(director_id: int, service: DirectorService = Depends()):
    return service.delete(director_id)