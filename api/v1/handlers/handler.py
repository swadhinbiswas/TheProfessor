from fastapi import APIRouter,HTTPException,UploadFile,File
from services import pdftoword
import pymongo 
from schemas import articleschema


routerx=APIRouter()

@routerx.post("/aticle",response_model=articleschema.ArticleOut)
async def store_article():
    pass
    