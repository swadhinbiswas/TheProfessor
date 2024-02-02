from typing import Optional, List
from uuid import UUID
from schemas.studentschemas import StudentBase,StudentOut,StudentUpdate
from models.studentmodel import Student
import pymongo

class StudentService:
  @staticmethod
  async def create_student(user:StudentBase):
    student_in=Student(
      student_id=user.student_id,
      first_name=user.first_name,
      last_name=user.last_name,
      user_name=user.user_name,
      email=user.email,
      hashed_password=user.hashed_password,
      is_active=user.is_active,
      is_superuser=user.is_superuser,
      userpicture=user.userpicture
    )
    await student_in.save()
    return student_in
  
  @staticmethod
  async def get_student_byid(student_id:str)->Optional[Student]:
    student=await Student.find_one(Student.student_id==student_id)
    return student
  
  @staticmethod
  async def get_student_byusername(username:str)->Optional[Student]:
    student=await Student.find_one(Student.user_name==username)
    return student
  
  @staticmethod
  async def get_student_byemail(email:str)->Optional[Student]:
    student=await Student.find_one(Student.email==email)
    return student
  
  @staticmethod
  async def update_student(student_id:str,student:StudentUpdate)->Optional[Student]:
    student=await Student.find_one(Student.student_id==student_id)
    if not student:
      raise pymongo.errors.OperationFailure("Student not found")
    
    await student.update({"$set":student.dict( exclude_unset=True)})
  
    return student
 