import os
import secrets

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException, Security
from fastapi.security import APIKeyHeader

load_dotenv()

API_KEY = os.environ["SERVICE_API_KEY"]
api_key_header = APIKeyHeader(name="X-API-Key")


def verify_api_key(provided_key: str = Security(api_key_header)) -> None:
    if not secrets.compare_digest(provided_key, API_KEY):
        raise HTTPException(status_code=401, detail="Invalid API key")


app = FastAPI()


@app.get("/protected", dependencies=[Depends(verify_api_key)])
def protected_route():
    return {"status": "ok"}
