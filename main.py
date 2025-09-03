from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.responses import PlainTextResponse;
app = FastAPI()

@app.get("/")
def read_root():
    return {"message" : "Bienvenue sur mon premier root"}

@app.get("/utilisateur/{nom}")
def dire_bonjour(nom: str):
    return {"message" : f"bonjour {nom}"}

@app.get("/health")
def get_health():
    return { "message" : "ok"}