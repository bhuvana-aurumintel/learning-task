from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message":"this is learning task"}
@app.get("/health")
def health_check():
    return {"":"health is good"}


