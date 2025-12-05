from typing import List
from fastapi import APIRouter, HTTPException

from app.db import movies_db
from app.models.movie import Movie, MovieCreate, MovieUpdate

router = APIRouter()

def _get_next_id() -> int:
    if not movies_db:
        return 1
    return max(movie["id"] for movie in movies_db) + 1


@router.get("/movies", response_model=List[Movie])
def list_movies() -> List[Movie]:
    return movies_db


@router.get("/movies/{movie_id}", response_model=Movie)
def get_movie(movie_id: int) -> Movie:
    for movie in movies_db:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")


@router.post("/movies", response_model=Movie, status_code=201)
def create_movie(payload: MovieCreate) -> Movie:
    new_movie = {
        "id": _get_next_id(),
        "title": payload.title,
        "release_year": payload.release_year,
        "genres": payload.genres,
        "rating": 0.0,
        "summary": payload.summary,
    }
    movies_db.append(new_movie)
    return new_movie


@router.put("/movies/{movie_id}", response_model=Movie)
def update_movie(movie_id: int, payload: MovieUpdate) -> Movie:
    for movie in movies_db:
        if movie["id"] == movie_id:
            if payload.title is not None:
                movie["title"] = payload.title
            if payload.release_year is not None:
                movie["release_year"] = payload.release_year
            if payload.genres is not None:
                movie["genres"] = payload.genres
            if payload.summary is not None:
                movie["summary"] = payload.summary
            return movie

    raise HTTPException(status_code=404, detail="Movie not found")


@router.delete("/movies/{movie_id}", status_code=204)
def delete_movie(movie_id: int) -> None:
    for index, movie in enumerate(movies_db):
        if movie["id"] == movie_id:
            movies_db.pop(index)
            return

    raise HTTPException(status_code=404, detail="Movie not found")
