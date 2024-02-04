from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from api.v1.handlers.teacherpannel import teacher_router
from routes import routersapp



app = FastAPI(title="Cheacker", 
              description="A simple ToDoApp", 
              version="1.0.0",)




@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(routersapp.app_router,prefix="/apiv1")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
