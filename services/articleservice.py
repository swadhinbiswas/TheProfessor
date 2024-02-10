from calendar import c
from os import path
import shutil
import pdftoword
from typing import Optional,List
from fastapi import File,UploadFile
from schemas.articleschema import ArticleSchema
from models.articlemodel import ArticleModel
import pymongo 

class ArticleService:
    @staticmethod
    async def create_article(user:ArticleSchema, uploade_file:UploadFile=File(...)):
        path=f"files/{uploade_file.filename}"
        with open(path, "wb") as buffer:
            shutil.copyfileobj(uploade_file.file, buffer)
            
        data=await pdftoword.pdftotext(path)
        


        article_in=ArticleModel(
            title=user.title,
            owner=user.owner,
            filename=uploade_file.filename,
            content=data,
        )
        await article_in.save()
        return article_in
    @staticmethod
    async def get_article_bytitle(title:str)->Optional[ArticleModel]:
        article=await ArticleModel.find_one(ArticleModel.title==title)
        return article 