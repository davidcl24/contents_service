from fastapi import APIRouter
from fastapi.params import Depends

from app.schemas.show import ShowResponse, ShowCreate, ShowUpdate
from app.services.show_service import ShowService

router = APIRouter(tags=["Shows"])

@router.post("/shows", response_model=ShowResponse)
async def create_show(show: ShowCreate, service: ShowService = Depends()):
    return service.create(show)

@router.get("/shows", response_model=list[ShowResponse])
async def read_shows(service: ShowService = Depends()):
    return service.get_all()

@router.get("/shows/{show_id}", response_model=ShowResponse)
async def read_show(show_id: int, service: ShowService = Depends()):
    return service.get_by_id(show_id)

@router.get("/genres/{genre_id}/shows", response_model=list[ShowResponse])
async def read_shows_by_genre(genre_id: int, service: ShowService = Depends()):
    return service.get_by_genre(genre_id)

@router.get("/actors/{actor_id}/shows", response_model=list[ShowResponse])
async def read_shows_with_actor(actor_id: int, service: ShowService = Depends()):
    return service.get_with_actor(actor_id)

@router.get("/directors/{director_id}/shows", response_model=list[ShowResponse])
async def read_shows_with_director(director_id: int, service: ShowService = Depends()):
    return service.get_with_director(director_id)

@router.post("/shows/batch", response_model=list[ShowResponse])
async def read_shows_batch(ids: list[int], service: ShowService = Depends()):
    return service.get_batch(ids)

@router.patch("/shows/{show_id}", response_model=ShowResponse)
async def update_show(show_id: int, show_data: ShowUpdate, service: ShowService = Depends()):
    return service.update(show_id, show_data)


@router.delete("/shows/{show_id}", response_model=dict)
async def delete_show(show_id: int, service: ShowService = Depends()):
    return service.delete(show_id)
