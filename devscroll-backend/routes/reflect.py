from fastapi import APIRouter
from models import ReflectionRequest
from database import get_db_connection

router = APIRouter()

@router.post("/reflect")
def reflect(request: ReflectionRequest):
    # Save to DB
    conn = get_db_connection()
    c = conn.cursor()
    c.execute(
        "INSERT INTO reflections (session_id, card_index, reflection_text) VALUES (?, ?, ?)",
        (request.session_id, request.card_index, request.reflection_text)
    )
    conn.commit()
    
    # Count how many reflections in this session to simulate a streak
    c.execute("SELECT COUNT(*) FROM reflections WHERE session_id = ?", (request.session_id,))
    row = c.fetchone()
    streak = row[0] if row else 1
    
    conn.close()
    
    return {
        "message": "Reflection saved", 
        "streak": streak
    }
