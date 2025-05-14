import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    if os.getenv("ENVIRONMENT") == "production":
        return {"AZFunc message": "You have mastered all the topics efficiently with azure app service instead of just a container instance - Updated with GitHub Actions!"}
    else:
        return {"message": "Yes you have mastered the concept - Local Version"}
    
    
@app.get("/version")
def get_version():
    return {"version": "1.0.1"} 