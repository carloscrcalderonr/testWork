from fastapi import FastAPI, BackgroundTasks
from api.v1.endpoints import router as api_router

app = FastAPI()

app.include_router(api_router, prefix="/v1")