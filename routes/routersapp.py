from fastapi import APIRouter, HTTPException, status
from api.v1.handlers import plaguehandel,teacherpannel,handler

app_router=APIRouter()

app_router.include_router(plaguehandel.router,prefix='/plagures',tags=["plagures"])
app_router.include_router(teacherpannel.teacher_router,prefix='/teachers',tags=["teachers"])
app_router.include_router(handler.routerx,prefix='/uplaodpf',tags=["uploadpdf"])

