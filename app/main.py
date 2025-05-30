from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="MCP Server for AWS HealthLake")

app.include_router(router)
