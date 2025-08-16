from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="TradePulse API", version="1.0.0") #start with uvicorn main:app --reload

@app.get("/")
async def root():
    return {"message": "Welcome to TradePulse API"}

@app.get("/health/{service_id}")
async def health_check(service_id: str):
    return {"status": "healthy", "service_id": service_id}