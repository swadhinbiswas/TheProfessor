# Auther: The Professor
from typing import Any, Optional
from datetime import datetime
from uuid import UUID,uuid4
from beanie import Document, Indexed, DocumentTemplate

class Student(Document):
    user_id: UUID = Indexed(default_factory=uuid4)
    student_id:Indexed(str,unique=True)
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
        return f"<Student {self.user_name}>",f"<Student {self.email}>",f"<Student {self.student_id}>"
    
    def __str__(self):
        return self.student_id,self.user_name,self.email
    
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False
    
    def __hash__(self)->int:
        return hash(self.student_id)
    
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    @property
    def create(self)->datetime:
        return self.created_at
    
    @classmethod 
    async def get_student(self,student_id:str)->"Student":
        return await Student.find_one(self.student_id == student_id)
    async def get_student_by_email(self,email:str)->"Student":
        return await Student.find_one(self.email == email)
    async def get_student_by_username(self,user_name:str)->"Student":
        return await Student.find_one(self.user_name == user_name)
    
    class Collection:
        name = "student"
    