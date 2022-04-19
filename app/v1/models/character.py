# Python
from uuid import UUID
from datetime import date
from typing import Optional

# Pydantic
from pydantic import (
    BaseModel, EmailStr, Field
)

class Character(BaseModel):
    id: str = Field(alias="_id")
    birth:Optional[str]=None
    death:Optional[str]=None
    hair:Optional[str]=None
    gender:Optional[str]=None
    height:Optional[str]=None
    realm:Optional[str]=None
    spouse:Optional[str]=None
    name:str
    race:Optional[str]=None
    wikiurl:Optional[str]=None

    class Config():
        schema_extra = {
            "example": {
                 "_id": "5cd99d4bde30eff6ebccfea7",
                "height": "Slightly larger and taller than a Man (book), 20 feet (movie)",
                "race": "Maiar",
                "gender": "Male",
                "birth": "Before the creation of ,Arda",
                "spouse": "",
                "death": "January 253019",
                "realm": "",
                "hair": "Mane of red flames",
                "name": "Durin's Bane",
                "wikiUrl": "http://lotr.wikia.com//wiki/Durin%27s_Bane"
            }
        }