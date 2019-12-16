import time
import tqdm

def print_1():
    for i in range(10):
        print("\r", i, flush=True, end="")
        time.sleep(0.4)


print_1()
