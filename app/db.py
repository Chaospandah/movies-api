from typing import List, Dict


movies_db: List[Dict] = [
    {
        "id": 1,
        "title": "Interstellar",
        "release_year": 2014,
        "genres": ["Sci-Fi", "Drama"],
        "rating": 9.0,
        "summary": "A NASA pilot travels through a wormhole to save humanity.",
    },
    {
        "id": 2,
        "title": "The Dark Knight",
        "release_year": 2008,
        "genres": ["Action", "Crime"],
        "rating": 9.1,
        "summary": "Batman faces the Joker in Gotham City.",
    },
]

# In-memory "database" for reviews
reviews_db: List[Dict] = []
