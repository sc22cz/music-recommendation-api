from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
import app.models
from app.routers import songs, artists

app = FastAPI(
    title="Music Recommendation API",
    description="A data-driven API for music discovery and personalised recommendations.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(songs.router)
app.include_router(artists.router)

@app.get("/")
def root():
    return {
        "message": "Music Recommendation API",
        "docs": "/docs",
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}
