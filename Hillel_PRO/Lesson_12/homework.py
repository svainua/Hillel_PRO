import os
import threading
import time
from dataclasses import dataclass
from multiprocessing import Process

import requests
from cryptography.fernet import Fernet


@dataclass
class Path:
    path: str


def encrypt_file(path: str):
    print(f"Processing file from {path} in process {os.getpid()}")
    key = Fernet.generate_key()
    with open("filekey.key", "wb") as filekey:
        filekey.write(key)
    with open("filekey.key", "rb") as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open(path, "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(path, "wb") as encrypted_file:
        encrypted_file.write(encrypted)


def download_image(image_url, image_path):
    print(
        f"Downloading image from {image_url} "
        f"in thread {threading.current_thread().name}"
    )
    response = requests.get(image_url)
    with open(image_path, "wb") as f:
        f.write(response.content)


text_file_path = Path(path="rockyou.txt")
image_path = Path(path="image.jpg")
url_image_path = Path(path="https://picsum.photos/1000/1000")


if __name__ == "__main__":

    try:
        start_proc = time.perf_counter()
        my_proc = Process(target=encrypt_file, args=(text_file_path.path,))
        my_proc.start()
        my_proc.join()
        encryption_counter = time.perf_counter() - start_proc

        start_thread = time.perf_counter()
        my_thread = threading.Thread(
            target=download_image, args=(url_image_path.path, image_path.path)
        )
        my_thread.start()
        my_thread.join()
        download_counter = time.perf_counter() - start_thread

        total = encryption_counter + download_counter

        print(
            f"Time taken for encryption task: {encryption_counter}, "
            f"I/O-bound task: {download_counter}, Total: {total} seconds"
        )
    except Exception as e:
        print(f"Error occurred: {e}")
