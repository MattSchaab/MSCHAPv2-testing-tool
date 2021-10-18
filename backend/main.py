from fastapi import FastAPI
import json

from RADIUS import RADIUS
from config import settings as s

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test")
async def root():
    configFile = {
        "RADIUS_HOST": s.RADIUS_HOST,
        "RADIUS_SECRET": s.RADIUS_SECRET,
        "RADIUS_NAS_IP": s.RADIUS_NAS_IP,
        "RADIUS_NAS_ID": s.RADIUS_NAS_ID,
        "USERNAME": s.USERNAME,
        "PASSWORD": s.PASSWORD
    }

    return {"message": json.dumps(configFile)}

@app.get("/radius")
async def root():
    r = RADIUS(s.RADIUS_HOST, s.RADIUS_SECRET, s.RADIUS_NAS_IP, s.RADIUS_NAS_ID)
    return {
        "message": r.is_credential_valid(s.USERNAME, s.PASSWORD)
    }