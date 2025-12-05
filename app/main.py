from fastapi import FastAPI

from app.routes.movies import router as movies_router
from app.routes.reviews import router as reviews_router

app = FastAPI(title="Movies API")


@app.get("/health")
def health_check():
    return {"status": "ok"}


# Include routers
app.include_router(movies_router)
app.include_router(reviews_router)
