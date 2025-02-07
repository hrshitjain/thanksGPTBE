from pydantic import BaseModel
from typing import Optional, List
import uuid

class GenericResponse(BaseModel):
    message: str
    session_id: Optional[str] = None

class Session(BaseModel):
    session_id: str = str(uuid.uuid4())  # Automatically generate unique session id
    action: Optional[str] = None
    required_params: Optional[List[str]] = None
    confirm_action: Optional[str] = None
