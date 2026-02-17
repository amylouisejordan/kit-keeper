from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Kit List API is running!"}
