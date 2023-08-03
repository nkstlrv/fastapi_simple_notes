import uvicorn
from fastapi import FastAPI
from routers import users, notes, authentication
from config.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(notes.router)
app.include_router(users.router)
app.include_router(authentication.router)


@app.get("/")
def index():
    return {"message": "Hello, there!"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
