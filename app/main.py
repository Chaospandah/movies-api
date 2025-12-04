from fastapi import FastAPI

app = FastAPI(title="Movies API")


@app.get("/health")
def health_check():
    return {"status": "ok"}
