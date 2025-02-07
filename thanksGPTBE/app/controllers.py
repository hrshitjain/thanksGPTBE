from fastapi import APIRouter, HTTPException, Depends
from services import handle_session
from models import Session, GenericResponse

router = APIRouter()

# Controller for starting the session
@router.post("/start-session", response_model=GenericResponse)
async def start_session():
    # Create a new session object
    session = Session()
    return GenericResponse(message="welcome", session_id=session.session_id)

# Controller for querying the service
@router.post("/query", response_model=GenericResponse)
async def query_service(query: str, session: Session = Depends(start_session)):
    response = await handle_session(session, query)
    return response
