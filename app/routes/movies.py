from typing import List
from fastapi import APIRouter, HTTPException

from app.models.movie import Movie, MovieCreate, MovieUpdate

router = APIRouter()

movies_db: List[dict] = [
    {"id": 1, 
     "title": "Interstellar", 
     "release_year": 2014, 
     "genre": ["Sci-Fi", "Drama"], 
     "summary": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.", 
     "rating": 8.6},

     {"id": 2,
      "title": "The Dark Knight",
      "release_year": 2008,
      "genre": ["Action", "Crime", "Drama"],
      "summary": "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.",
      "rating": 9.0}
]

def _get_next_id() -> int:
    if not movies_db:
        return 1
    return max(movie["id"] for movie in movies_db) + 1

@router.get("/movies", response_model=List[Movie])
def list_movies():
    return movies_db

@router.post("/movies", response_model=Movie, status_code=201)
def create_movie(payload: MovieCreate):
    new_movie = {
        "id": _get_next_id(),
        "title": payload.title,
        "release_year": payload.release_year,
        "genre": payload.genre,
        "rating": 0.0,
        "summary": payload.summary
    }
    movies_db.append(new_movie)
    return new_movie

@router.put("/movies/{movie_id}", response_model=Movie)
def update_movie(movie_id: int, payload: MovieUpdate):
    for movie in movies_db:
        if movie["id"] == movie_id:
            if payload.title is not None:
                movie["title"] = payload.title
            if payload.release_year is not None:
                movie["release_year"] = payload.release_year
            if payload.genre is not None:
                movie["genre"] = payload.genre
            if payload.summary is not None:
                movie["summary"] = payload.summary
            return movie
        
    raise HTTPException(status_code=404, detail="Movie not found")

@router.delete("/movies/{movie_id}", status_code=204)
def delete_movie(movie_id: int):
    for index, movie in enumerate(movies_db):
        if movie["id"] == movie_id:
            del movies_db[index]
            return
    raise HTTPException(status_code=404, detail="Movie not found")