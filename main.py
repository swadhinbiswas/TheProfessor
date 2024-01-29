from fastapi import FastAPI


app = FastAPI(title="Cheacker", 
              description="A simple ToDoApp", 
              version="1.0.0",)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
