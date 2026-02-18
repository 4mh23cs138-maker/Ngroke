from fastapi import FastAPI

from app.db.database import Base, engine
from app.routes.users import router as users_router

app = FastAPI(title="FastAPI SQLAlchemy User API")


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def hello_world():
    return {"message": "Hello World"}


app.include_router(users_router)
