from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import os
from dotenv import load_dotenv

load_dotenv()

# Database initialization occurs on import of this module
import database  
from routes import feed, reflect

app = FastAPI(title="DevScroll API")

# Allow all origins (standard FastAPI CORS middleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=600,
)

app.include_router(feed.router)
app.include_router(reflect.router)

@app.get("/")
@app.get("/health")
def health_check():
    return {"status": "ok", "model": "gemini-3-flash-preview"}
