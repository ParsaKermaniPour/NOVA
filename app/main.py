from fastapi import FastAPI
from pydantic import BaseModel
from app.agents import supervisor_agent
import uvicorn

app = FastAPI()

class Query(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/query")
def handle_query(request: Query):
    return {"message": supervisor_agent.process_query(request.query)}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080, log_level="info")