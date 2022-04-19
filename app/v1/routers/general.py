# Python
import sys
sys.path.append("..")

# FastAPI
from fastapi import (
    APIRouter, status, Body, HTTPException
)

router = APIRouter()

@router.get(
            path='/',
            status_code=status.HTTP_200_OK,
            summary='Hello World',
            tags=['General'])

def home():
    """Hello World Route.

    This path shows the classic Hello World message

    Parameters:
    - 

    Returns a json object with a simple Hello World

    """
    return {"message": "Hello World"}

