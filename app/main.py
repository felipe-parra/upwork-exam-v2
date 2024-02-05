from fastapi import FastAPI

from .database import Base, engine
from .api import user, profile

app = FastAPI(
    docs_url="/"
)

Base.metadata.create_all(bind=engine)


app.include_router(user.router)
app.include_router(profile.router)
