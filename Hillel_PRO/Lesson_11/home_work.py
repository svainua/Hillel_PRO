from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Post:
    message: str
    timestamp: int


class SocialChannel(ABC):
    def __init__(self, network: str, follower: int) -> None:
        self.network = network
        self.follower = follower

    @abstractmethod
    def make_a_post(self, message):
        pass


class YouTube(SocialChannel):
    def make_a_post(self, message):
        print(f"This is post for {self.network} with message {message}")


class Facebook(SocialChannel):
    def make_a_post(self, message):
        print(f"This is post for {self.network} with message {message}")


class Twitter(SocialChannel):
    def make_a_post(self, message):
        print(f"This is post for {self.network} with message {message}")


def post_a_message(channel: SocialChannel, message: str) -> None:
    channel.make_a_post(message)


def time() -> int:
    current_time = datetime.now()
    return int(current_time.strftime("%H"))


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    for post in posts:
        message, timestamp = post.message, post.timestamp
        for channel in channels:
            if timestamp <= time():
                post_a_message(channel, message)


current_time = datetime.now()
hour = current_time.strftime("%H")

post_1 = Post(message="Hello today", timestamp=10)
post_2 = Post(message="Hello tomorrow", timestamp=13)
post_3 = Post(message="Hello day after tomorrow", timestamp=17)

process_schedule(
    posts=[post_1, post_2, post_3],
    channels=[
        YouTube(network="youtube", follower=500),
        Facebook(network="facebook", follower=1000),
        Twitter(network="twitter", follower=30000),
    ],
)
