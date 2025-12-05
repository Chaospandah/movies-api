from fastapi import FastAPI

from app.routes.movies import router as movies_router

app = FastAPI(title="Movies API")


@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(movies_router)
