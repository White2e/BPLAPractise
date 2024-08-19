from memory_profiler import profile


@profile
def my_func():
    for i in range(100000):
        pass


if __name__ == '__main__':
    my_func()

