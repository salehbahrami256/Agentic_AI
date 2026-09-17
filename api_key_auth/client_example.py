import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["SERVICE_API_KEY"]

response = requests.get(
    "http://localhost:8000/protected",
    headers={"X-API-Key": API_KEY},
)
response.raise_for_status()
print(response.json())
