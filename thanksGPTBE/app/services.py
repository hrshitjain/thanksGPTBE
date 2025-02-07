from models import Session, GenericResponse
from adapters import call_gpt_api, call_ner_api, process_safecustody_action

async def handle_session(session: Session, query: str) -> GenericResponse:
    # Step 1: Check if action exists in session
    if not session.action:
        # If no action, call GPT API to determine intent
        intent = await call_gpt_api(query)
        if intent == "Negative":
            return GenericResponse(message="I couldn't understand your request, please try again.")
        
        # If Positive, set the action in the session
        session.action = intent
    
    # Step 2: Check if required parameters exist
    if not session.required_params:
        # Call NER API to extract parameters
        params = await call_ner_api(query)
        if not params:
            return GenericResponse(message="I need more information to proceed.")
        
        session.required_params = params
    
    # Step 3: Confirm the action
    if session.confirm_action is None:
        return GenericResponse(message="Do you confirm the action? Yes/No")
    
    if session.confirm_action == "Yes":
        # Process Safecustody action
        result = await process_safecustody_action(session)
        session.action = None  # Terminate session after action
        return GenericResponse(message="Success! Your request has been processed.")

    if session.confirm_action == "No":
        # Terminate session
        session.action = None
        return GenericResponse(message="Session terminated.")

    # Default if confirmation is still pending
    return GenericResponse(message="Waiting for confirmation: Yes/No.")
