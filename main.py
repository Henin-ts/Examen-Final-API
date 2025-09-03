from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.responses import PlainTextResponse;
from fastapi.responses import JSONResponse; 

app = FastAPI()

@app.get("/health")
def get_health():
    return { "message" : "ok"}


@app.post("/phones")
def create_liste(idedentifier : str , brand : str , modele : str , characteristics : object  ):
    return {idedentifier , brand , modele , characteristics}