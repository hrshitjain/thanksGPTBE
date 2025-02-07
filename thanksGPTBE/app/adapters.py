import random

# Simulate GPT API call for intent detection
async def call_gpt_api(query: str) -> str:
    # Example GPT logic for simplicity
    if "stop service" in query.lower():
        return "Stop Service"
    return "Unknown Intent"

# Simulate NER API to extract parameters from the user's query
async def call_ner_api(query: str) -> list:
    # Example NER logic (extracting dummy parameters for simplicity)
    if "broadband" in query.lower():
        return ["broadband"]
    return []

# Simulate Safecustody downstream service processing
async def process_safecustody_action(session):
    # Simulate a process based on the session details
    if "broadband" in session.required_params:
        return True
    return False
