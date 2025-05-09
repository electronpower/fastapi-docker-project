import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    if os.getenv("ENVIRONMENT") == "production":
        return {"message": "You have mastered all the topics efficiently"}
    else:
        return {"message": "Yes you have mastered the concept"}
    
@app.get("/version")
def get_version():
    return {"version": "1.0.0"}