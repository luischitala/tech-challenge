

# FastAPI
from fastapi import FastAPI

# Routers
from routers.general import router as general_router
from routers.lod import router as lod_router

# Initialize the app
app = FastAPI()

# V1
app.include_router(general_router, prefix='/v1')
app.include_router(lod_router, prefix='/v1/lod')
