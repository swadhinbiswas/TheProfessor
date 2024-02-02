from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel,EmailStr,Field
from models.plagermodel import Plager

class PlagerBase(BaseModel):
    file_name: str=Field(...,description="Name of the file")
    title: str=Field(...,description="Title of the file")
    owner: List[str]=Field(...,description="Owner of the file")
    plagarism: str=Field(...,description="Plagarism of the file")
    description: str=Field(...,description="Description of the file")
   
class OutPlager(PlagerBase):
    file_name: str
    title: str
    owner: List[str]
    plagarism: str
    description: str
    
class UpdatePlager(BaseModel):
    file_name: Optional[str]
    title: Optional[str]



