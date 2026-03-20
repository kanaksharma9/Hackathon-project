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

# Allow all origins (this is a hackathon) — explicit for Railway proxy
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"],
    max_age=600,
)

# Explicit catch-all OPTIONS handler to fix CORS 405 preflight on Railway
@app.options("/{rest_of_path:path}")
async def preflight_handler(rest_of_path: str, request: Request):
    return Response(
        status_code=200,
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers": "*",
        }
    )

app.include_router(feed.router)
app.include_router(reflect.router)

@app.get("/health")
def health_check():
    return {"status": "ok", "model": "gemini-3-flash-preview"}
