from fastapi import APIRouter
from fastapi.params import Depends

from app.schemas.episode import EpisodeCreate, EpisodeResponse, EpisodeUpdate
from app.services.episode_service import EpisodeService

router = APIRouter(tags=["Episodes"])

@router.post("/episodes", response_model=EpisodeResponse)
async def create_episode(episode: EpisodeCreate, service: EpisodeService = Depends()):
    return service.create(episode)

@router.get("/shows/{show_id}/episodes", response_model=list[EpisodeResponse])
async def read_episodes_from_show(show_id: int, service: EpisodeService = Depends()):
    return service.get_all_from_show(show_id)

@router.get("/shows/{show_id}/{season_num}/episodes", response_model=list[EpisodeResponse])
async def read_episodes_from_show_by_season(show_id: int, season_num: int, service: EpisodeService = Depends()):
    return service.get_from_show_by_season(show_id, season_num)

@router.get("episodes/{episode_id}", response_model=EpisodeResponse)
async def read_episode(episode_id: int, service: EpisodeService = Depends()):
    return service.get_by_id(episode_id)

@router.patch("episodes/{episode_id}", response_model=EpisodeResponse)
async def update_episode(episode_id: int, episode_data: EpisodeUpdate, service: EpisodeService = Depends()):
    return service.update(episode_id, episode_data)

@router.delete("episodes/{episode_id}", response_model=dict)
async def delete_episode(episode_id: int, service: EpisodeService = Depends()):
    return service.delete(episode_id)