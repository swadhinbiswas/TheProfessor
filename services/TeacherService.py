from typing import Optional, List
from uuid import UUID
from schemas.teacher_shema import OutTeacher,UpdateTeacher,TeacherBase
from models.TeachersMOdel import Teacher

import pymongo

class TeacherService:
    @staticmethod
    async def create_teacher(user:TeacherBase):
        teacher_in=Teacher(
            teacher_id=user.teacher_id,
            name=user.name,
            email=user.email,
            username=user.username,
            password=user.password,
            frist_name=user.frist_name,
            last_name=user.last_name,
            
        )
        await teacher_in.save()
        return teacher_in
    
    @staticmethod
    async def get_teacher_byid(teacher_id:str)->Optional[Teacher]:
      teacher=await Teacher.find_one(Teacher.teacher_id==teacher_id)
      return teacher
  
    @staticmethod
    async def get_teacher_byusername(username:str)->Optional[Teacher]:
      teacher=await Teacher.find_one(Teacher.username==username)
      return teacher
  
    @staticmethod
    async def get_teacher_byemail(email:str)->Optional[Teacher]:
      teacher=await Teacher.find_one(Teacher.email==email)
      return teacher
  
    @staticmethod
    async def get_teacher_byname(name:str)->Optional[Teacher]:
      teacher=await Teacher.find_one(Teacher.name==name)
      return teacher
  
    @staticmethod         
    async def get_all_teachers()->List[Teacher]:
      teachers=await Teacher.find_all()
      return teachers
    
    @staticmethod
    async def update_teacher(teacher_id:str,teacher:UpdateTeacher)->Optional[Teacher]:
      teacher=await Teacher.find_one(Teacher.teacher_id==teacher_id)
      if not teacher:
        raise pymongo.errors.OperationFailure("Teacher not found")
      
      await teacher.update({"$set":teacher.dict( exclude_unset=True)})
    
      return teacher