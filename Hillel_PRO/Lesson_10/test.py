import datetime
import json

results = {"results": []}


def write_to_file(
    currency_from: str, currency_to: str, rate: str, date: str
):  # noqa
    content: dict = {
        "currency_from": currency_from,
        "currency_to": currency_to,
        "rate": rate,
        "timestamp": date,
    }
    # with open("logs.json", mode="a") as file:
    #     json.dump(content, file)
    results["results"].append(content)


currency_from: str = "UAH"
currency_to: str = "USD"
rate: str = "0.025"

fulldate = datetime.datetime.now()
date_and_time: str = fulldate.strftime("%d/%m/%Y at %H:%M:%S")

write_to_file(
    currency_from=currency_from,
    currency_to=currency_to,
    rate=rate,
    date=date_and_time,
)

with open("logs.json", mode="a") as file:
    json.dump(results, file, indent=4)
