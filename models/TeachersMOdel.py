#Auther :The Professor

from typing import Any, Optional
from datetime import datetime
from uuid import UUID,uuid4
from beanie import Document, Indexed

class Teacher(Document):
    user_id: UUID = Indexed(default_factory=uuid4)
    teacher_id:Indexed(str,unique=True)
    teacher_deg:Optional[str] = None
    teacher_profile:Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    user_name:Indexed(str,unique=True)
    email:Indexed(str,unique=True)
    hashed_password: str 
    is_active:Optional[bool] = True
    is_superuser: Optional[bool] = False
    created_at: Optional[datetime] = datetime.now()
    userpicture:Optional[str] = None
    
    
    
    def __repr__(self):
        return f"<Teacher {self.user_name}>",f"<Teacher {self.email}>",f"<Teacher {self.teacher_id}>"
    
    def __str__(self):
        return self.teacher_id,self.user_name,self.email
    
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Teacher):
            return self.teacher_id == other.teacher_id
        return False
    
    def __hash__(self)->int:
        return hash(self.teacher_id)
    
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    @property
    def create(self)->datetime:
        return self.created_at
    
    @classmethod 
    async def get_teacher(self,teacher_id:str)->"Teacher":
        return await Teacher.find_one(self.teacher_id == teacher_id)
    async def get_teacher_by_email(self,email:str)->"Teacher":
        return await Teacher.find_one(self.email == email)
    async def get_teacher_by_username(self,user_name:str)->"Teacher":
        return await Teacher.find_one(self.user_name == user_name)
    
    class Collection:
        name = "teacher"