import time
import math


def slow_func():
    result = 0
    for i in range(1, 1000000):
        result += math.sqrt(i)
    return result


if __name__ == '__main__':
    print("Start func")
    time.sleep(2)
    slow_func()
    print("End func")

