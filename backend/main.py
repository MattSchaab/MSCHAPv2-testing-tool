from fastapi import FastAPI

from RADIUS import RADIUS

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

radius_host = '10.1.2.3'
radius_secret = 'r4d!us_$3cr3t'
radius_nas_ip = '10.3.2.1'
radius_nas_id = 'mynas'
username = 'myuser'
password = 'mypassword!'

@app.get("/radius")
async def root():
    r = RADIUS(radius_host, radius_secret, radius_nas_ip, radius_nas_id)
    return {
        "message": r.is_credential_valid(username, password)
    }