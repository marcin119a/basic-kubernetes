from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Hello from FastAPI in Kubernetes!"}

@app.get("/ping")
def ping():
    return {"status": "ok"}
