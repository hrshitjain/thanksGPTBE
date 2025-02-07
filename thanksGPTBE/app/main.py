from fastapi import FastAPI
from controllers import router as controller_router

app = FastAPI()

# Include the controller routes
app.include_router(controller_router)
