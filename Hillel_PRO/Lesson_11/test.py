from dataclasses import dataclass
from datetime import datetime


@dataclass
class Body:
    leg: str
    body: str


my_body = Body(leg="left_leg", body="my_body")


def take_part(my_body):
    leg, body = my_body.leg, my_body.body
    print(leg)
    print(body)


take_part(my_body=my_body)


time = datetime.now()
hour = time.strftime("%H")
print(type(hour))
