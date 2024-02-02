from typing import Optional, List
from uuid import UUID
from fastapi import APIRouter,Depends,HTTPException,status
from services import TeacherService
from models import *
from schemas.teacher_shema import OutTeacher,UpdateTeacher,TeacherBase
import pymongo

  
teacher_router = APIRouter()

@teacher_router.post("/teacher",response_model=OutTeacher)
async def create_teacher(data:TeacherBase):
  try:
      return await TeacherService.create_teacher(data)
  except pymongo.errors.DuplicateKeyError:
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                          detail="Username already exists")
  
  
@teacher_router.post("/update_teacher",
                     response_model=OutTeacher)
async def update_teacher(data:UpdateTeacher):
    try:
        return await TeacherService.update_teacher(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="user Does not exists")


