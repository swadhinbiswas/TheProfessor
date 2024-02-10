from typing import List,Optional
from pydantic import BaseModel,Field
from fastapi import File,UploadFile

class ArticleSchema(BaseModel):
    title: str = Field(...)
    content:str=Field(...)
    owner: List[str] = Field(...)
    filename:str=Field(...)
    

class ArticleOut(BaseModel):
    title: str
    owner: List[str]
    content:str

    


