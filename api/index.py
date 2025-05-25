from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load marks data from JSON file
json_path = os.path.join(os.path.dirname(__file__), "..", "q-vercel-python.json")
with open(json_path) as f:
    marks_data = json.load(f)

@app.get("/api")
def get_marks(name: list[str] = Query(None)):
    if not name:
        return {"marks": []}
    result = [marks_data.get(n, None) for n in name]
    return {"marks": result}
