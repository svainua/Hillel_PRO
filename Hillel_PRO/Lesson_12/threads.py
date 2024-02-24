import random
import string
import time
from multiprocessing import Process
from threading import Thread


def task(n):
    items: list[str] = []
    for _ in range(n):
        word = "".join([random.choice(string.ascii_letters) for _ in range(3)])
        items.append(word)

    del items


def sequential():
    task(1_000_000)
    task(2_000_000)


def using_threads():
    threads: list[Thread] = [
        Thread(target=task, args=(1_000_000,)),
        Thread(target=task, args=(2_000_000,)),
    ]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    start = time.perf_counter()

    # sequential()
    using_threads()

    print(f"Total: {time.perf_counter() - start}")


# =====================================================================
# I/O bound

# def io_bound(n):
#     time.sleep(n)


# def sequential():
#     io_bound(2)
#     io_bound(3)


# def using_threads():
#     threads: list[Thread] = [
#         Thread(target=io_bound, args=(2,)),
#         Thread(target=io_bound, args=(3,))
#     ]
#     for thread in threads:
#         thread.start()

#     for thread in threads:
#         thread.join()


# if __name__== "__main__":
#     start = time.perf_counter()

#     #sequential()
#     using_threads()

#     print(f"Total: {time.perf_counter() - start}")

# =========================================================================================

# Multiprocessing (CPU)

# CPU bound

# def cpu_bound(n):
#     items: list[str] = []
#     for _ in range(n):
#         word = "".join([random.choice(string.ascii_letters) for _ in range(3)])
#         items.append(word)

#     del items


# def sequential():
#     cpu_bound(1_000_000)
#     cpu_bound(2_000_000)


# def using_threads():
#     threads: list[Process] = [
#         Process(target=cpu_bound, args=(1_000_000,)),
#         Process(target=cpu_bound, args=(2_000_000,))
#     ]

#     for thread in threads:
#         thread.start()

#     for thread in threads:
#         thread.join()


# if __name__== "__main__":
#     start = time.perf_counter()

#     #sequential()
#     using_threads()

#     print(f"Total: {time.perf_counter() - start}")


# ==================================================================


# thread = threading.Thread(target=task, args=(200_000, ))
# thread.start() # начать поток
# thread.join() # дождаться завершения

# CPU Bound - привязана к CPU

# I/O Bound - привязана к вводу и выводу    ---> promt это input, когда ввожите информацию.
# ждем инпут - это называется I/O задача. аутпут - это когда выводим инфу.
