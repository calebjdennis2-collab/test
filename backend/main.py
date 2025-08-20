from fastapi import FastAPI

app = FastAPI(title="Docu Cloud API")

@app.get("/")
async def read_root():
    return {"msg": "Welcome to Docu Cloud API!"}
