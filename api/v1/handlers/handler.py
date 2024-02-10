from fastapi import APIRouter,HTTPException,UploadFile,File
from fastapi.responses import JSONResponse

import pymongo 
from schemas import articleschema
import shutil
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Callable

routerx=APIRouter()

@routerx.post("/aticle",response_model=articleschema.ArticleOut)
async def create_upload_file(uploaded_file: UploadFile = File(...)):
    file_location = f"files/{uploaded_file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())
    return {"info": f"file '{uploaded_file.filename}' saved at '{file_location}'"}

