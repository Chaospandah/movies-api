from typing import List, Optional

from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    release_year: int
    genres: List[str]
    summary: str


class MovieCreate(MovieBase):
    pass


class MovieUpdate(BaseModel):
    title: Optional[str] = None
    release_year: Optional[int] = None
    genres: Optional[List[str]] = None
    summary: Optional[str] = None


class Movie(MovieBase):
    id: int
    rating: Optional[float] = None
