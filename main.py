from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Job Ecosystem Running 🚀"}
