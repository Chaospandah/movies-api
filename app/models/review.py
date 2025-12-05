from pydantic import BaseModel, conint


class ReviewBase(BaseModel):
    reviewer: str
    rating: conint(ge=1, le=10)
    comment: str


class ReviewCreate(ReviewBase):
    pass


class Review(ReviewBase):
    id: int
    movie_id: int
