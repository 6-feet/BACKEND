from fastapi import FastAPI

from core.routes import authorization, default


app = FastAPI()
app.include_router(authorization.router)
app.include_router(default.router)
