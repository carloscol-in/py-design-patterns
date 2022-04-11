import time


def time_it(func):
    """Time-it decorator.

    Args:
        func (Function): Function to measure execution time from.
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func()
        end = time.time()
        print(f'Function {func.__name__} took {round(end - start, 4)}s to run.')
        return result
    return wrapper

@time_it
def some_op():
    print('Starting the operation')
    time.sleep(1)
    print('Done with the operation')
    return 123

if __name__ == '__main__':
    print(some_op())