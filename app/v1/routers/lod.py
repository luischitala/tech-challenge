# Python
import json
import sys
sys.path.append("..")
from typing import (
    List, Optional
    )

# Requests
import httpx

# FastAPI
from fastapi import (
    APIRouter, status, Query
)

#Settings
from config import settings
API_KEY = settings.SECRET_KEY
BEARER_AUTH = 'Bearer ' + API_KEY

# Models
from models.character import Character

router = APIRouter()

PUBLIC_URL = "https://the-one-api.dev/v2/book"
URL = "https://the-one-api.dev/v2"

def get_characters(limit=None) -> dict:
    url = URL + '/character'
    if limit != None:
        url+='?limit='+str(limit)
    client = httpx.Client()
    headers = {'Authorization': BEARER_AUTH}
    response = client.get(url, headers=headers)
    json_response = response.json()['docs']
    return json_response 

@router.get(
    path='/character',
    response_model=List[Character],
    status_code=status.HTTP_200_OK,
    summary='Get all Characters',
    tags=['Lord of the Rings']
    )

def get_chars(limit: Optional[int] = Query(
        None, 
        gt=0, 
        le=100,
        title="Limit",
        description="This is limit of Characters to show",
        example=10
        ),):
    """Characters from the Lord of the Rings API.

    https://the-one-api.dev/documentation

    This path shows the 933 Characters from Lord of the Rings

    Parameters:
    - (Optional) Limit

    Returns a json object with a the result

    """
    return get_characters(limit)


