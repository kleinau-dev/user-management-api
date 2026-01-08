from fastapi import FastAPI

app = FastAPI(title="User Management API")

@app.get("/")
def read_root():
    return {"message": "API funcionando"}
