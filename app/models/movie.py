from pydantic import BaseModel
from typing import List, Optional

class MovieBase(BaseModel):
    title: str
    release_year: int
    genre: List[str]
    summary: str

class MovieCreate(MovieBase):
    pass

class MovieUpdate(BaseModel):
    title: Optional[str] = None
    relase_year: Optional[int] = None
    genre: Optional[List[str]] = None
    summary: Optional[str] = None

class Movie(MovieBase):
    id: int
    rating: Optional[float] = None


