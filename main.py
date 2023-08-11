from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount the 'static' directory to serve CSS files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Import the routes defined in routes.py and add them to the FastAPI application
from app import routes
app.include_router(routes.router)
