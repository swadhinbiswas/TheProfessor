from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel,EmailStr,Field
from models.studentmodel import Student

class StudentBase(BaseModel):
    name: str=Field(...,description="Name of the student")
    email: EmailStr=Field(...,description="Email of the student")
    username: str=Field(...,min_length=5,max_length=23,description="Username of the student")
    password: str=Field(...,min_length=8,max_length=23,description="Password of the student")
    frist_name: Optional[str]=Field(None,description="First name of the student")
    last_name: Optional[str]=Field(None,description="Last name of the student")
    is_active: Optional[bool]=Field(True,description="Is the student active")
    is_superuser: Optional[bool]=Field(False,description="Is the student superuser")
    userpicture: Optional[str]=Field(None,description="Profile picture of the student")
    

class StudentOut(BaseModel):
    name: str=Field(...,description="Name of the student")
    email: EmailStr=Field(...,description="Email of the student")
    username: str=Field(...,min_length=5,max_length=23,description="Username of the student")
    frist_name: Optional[str]=Field(None,description="First name of the student")
    last_name: Optional[str]=Field(None,description="Last name of the student")
    is_active: Optional[bool]=Field(True,description="Is the student active")
    is_superuser: Optional[bool]=Field(False,description="Is the student superuser")
    userpicture: Optional[str]=Field(None,description="Profile picture of the student")
    
    
class StudentUpdate(BaseModel):
    name: Optional[str]=Field(None,description="Name of the student")
    email: Optional[EmailStr]=Field(None,description="Email of the student")
    username: Optional[str]=Field(None,min_length=5,max_length=23,description="Username of the student")
    frist_name: Optional[str]=Field(None,description="First name of the student")
    last_name: Optional[str]=Field(None,description="Last name of the student")
    is_active: Optional[bool]=Field(None,description="Is the student active")
    is_superuser: Optional[bool]=Field(None,description="Is the student superuser")
    userpicture: Optional[str]=Field(None,description="Profile picture of the student")
    