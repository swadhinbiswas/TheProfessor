from fastapi import APIRouter, HTTPException, status
from api.v1.handlers import plaguehandel,teacherpannel

app_router=APIRouter()

app_router.include_router(plaguehandel.router,prefix='/plagures',tags=["plagures"])
app_router.include_router(teacherpannel.teacher_router,prefix='/teachers',tags=["teachers"])

