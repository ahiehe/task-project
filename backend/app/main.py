from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from .database import Base, engine
from .routes.task import router
from .routes.user import user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)
app.include_router(user_router)