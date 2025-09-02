from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message" : "Bienvenue sur mon premier root"}

@app.get("/utilisateur/{nom}")
def dire_bonjour(nom: str):
    return {"message" : f"bonjour {nom}"}
