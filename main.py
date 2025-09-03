from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.responses import JSONResponse; 

app = FastAPI()

@app.get("/health")
def get_health():
    return { "message" : "ok"}


@app.post("/phones")
def create_liste(identifier : str , brand : str , modele : str  ):
    return { JSONResponse : ( identifier , brand , modele )}



@app.get("/phones")
def phone():
    return {}


