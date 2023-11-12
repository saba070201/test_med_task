from .services import get_openings
from fastapi import FastAPI
app = FastAPI()
@app.get("/openings/")
def get_questions():
    return get_openings()
