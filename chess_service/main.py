from fastapi import FastAPI
from chess_service.routers import router

app = FastAPI()

app.include_router(router.router)
