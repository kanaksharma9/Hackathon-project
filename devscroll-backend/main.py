from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

# Database initialization occurs on import of this module
import database  
from routes import feed, reflect

load_dotenv()

app = FastAPI(title="DevScroll API")

# Allow all origins (this is a hackathon) — be explicit for Railway proxying
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=600,
)

app.include_router(feed.router)
app.include_router(reflect.router)

@app.get("/health")
def health_check():
    return {"status": "ok", "model": "gemini-3-flash-preview"}
