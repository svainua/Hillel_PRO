import random
import string
from typing import Callable

import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

create_random_string: Callable[[int], str] = lambda size: "".join(  # noqa
    [random.choice(string.ascii_letters) for i in range(size)]  # noqa
)  # noqa


@app.get("/generate-article")
async def get_information():
    """This endpoint returns the random information"""

    return {
        "title": create_random_string(size=10),
        "description": create_random_string(size=20),
    }


@app.get("/fetch-market")
async def get_current_market_state():
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=XSN17SDSA5RAM5W2"
    async with httpx.AsyncClient() as client:
        response: httpx.Response = await client.get(url)
    rate: str = response.json()["Realtime Currency Exchange Rate"][
        "5. Exchange Rate"
    ]
    return {
        "rate": rate,
    }
