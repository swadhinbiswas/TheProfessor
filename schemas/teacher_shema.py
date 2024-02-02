from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel,EmailStr,Field
from models.TeachersMOdel import Teacher

class TeacherBase(BaseModel):
    teacher_id: str=Field(...,description="ID of the teacher")
    teacher_deg: Optional[str]=Field(None,description="Degree of the teacher")
    teacher_profile: Optional[str]=Field(None,description="Profile of the teacher")
    name: str=Field(...,description="Name of the teacher")
    email: EmailStr=Field(...,description="Email of the teacher")
    username: str=Field(...,min_length=5,max_length=23,description="Username of the teacher")
    password: str=Field(...,min_length=8,max_length=23,description="Password of the teacher")
    frist_name: Optional[str]=Field(None,description="First name of the teacher")
    last_name: Optional[str]=Field(None,description="Last name of the teacher")
    is_active: Optional[bool]=Field(True,description="Is the teacher active")
    is_superuser: Optional[bool]=Field(False,description="Is the teacher superuser")
    userpicture: Optional[str]=Field(None,description="Profile picture of the teacher")
    

class OutTeacher(TeacherBase):
    teacher_id: str
    user_id: UUID
    teacher_deg: Optional[str]
    teacher_profile: Optional[str]
    name: str
    email: EmailStr
    username: str
    frist_name: Optional[str]
    last_name: Optional[str]
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    userpicture: Optional[str]
    

class UpdateTeacher(BaseModel):
    teacher_deg: Optional[str]
    teacher_profile: Optional[str]
    name: Optional[str]
    email: Optional[EmailStr]
    username: Optional[str]
    frist_name: Optional[str]
    last_name: Optional[str]
    userpicture: Optional[str]
