from typing import List
from fastapi import APIRouter, HTTPException

from app.db import movies_db, reviews_db
from app.models.review import Review, ReviewCreate

router = APIRouter()


def _get_next_review_id() -> int:
    """
    Get the next review ID based on the current max id in reviews_db.
    """
    if not reviews_db:
        return 1
    return max(review["id"] for review in reviews_db) + 1


def _ensure_movie_exists(movie_id: int) -> None:
    """
    Raise 404 if the given movie_id does not exist in movies_db.
    """
    for movie in movies_db:
        if movie["id"] == movie_id:
            return
    raise HTTPException(status_code=404, detail="Movie not found")


@router.get("/movies/{movie_id}/reviews", response_model=List[Review])
def list_reviews_for_movie(movie_id: int) -> List[Review]:
    """
    Return all reviews for a given movie.
    """
    _ensure_movie_exists(movie_id)
    return [review for review in reviews_db if review["movie_id"] == movie_id]


@router.post("/movies/{movie_id}/reviews", response_model=Review, status_code=201)
def create_review_for_movie(movie_id: int, payload: ReviewCreate) -> Review:
    """
    Create a new review for a specific movie.
    """
    _ensure_movie_exists(movie_id)

    new_review = {
        "id": _get_next_review_id(),
        "movie_id": movie_id,
        "reviewer": payload.reviewer,
        "rating": payload.rating,
        "comment": payload.comment,
    }
    reviews_db.append(new_review)
    return new_review


@router.delete("/reviews/{review_id}", status_code=204)
def delete_review(review_id: int) -> None:
    """
    Delete a review by its ID.
    """
    for index, review in enumerate(reviews_db):
        if review["id"] == review_id:
            reviews_db.pop(index)
            return

    raise HTTPException(status_code=404, detail="Review not found")
