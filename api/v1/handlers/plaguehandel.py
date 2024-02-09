from fastapi import APIRouter,Depends,HTTPException,status,Response
from services import findPlager
from schemas.plagur import OutPlager,PlagerBase,UpdatePlager
from models import plagermodel
from typing import List
import pymongo 
from fastapi.security import HTTPBearer


router = APIRouter()
token_auth = HTTPBearer()


@router.get("/",response_model=OutPlager)
async def get_plague(data:PlagerBase,token: str = Depends(token_auth)):
    pass

@router.get("/all",response_model=List[OutPlager])
async def get_all_plague():
    return await plagermodel.get_plague()

@router.post("/",response_model=OutPlager)
async def create_plague(data:PlagerBase):
    return await plagermodel.create_plague(data)

@router.put("/{title}",response_model=OutPlager)

async def update_plague(title:str,data:UpdatePlager):
    findPlague=await plagermodel.get_plague(title)
    if not findPlague:
        raise HTTPException(status_code=404,detail="Plague not found")
    return await plagermodel.update_plague(title,data)
    