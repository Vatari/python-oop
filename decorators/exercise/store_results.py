class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        with open("results.txt", "a") as file:
            result = self.func(*args, **kwargs)
            file.write(f"Function '{self.func.__name__}' was called. Result: {result}\n")


@store_results
def add(a, b):
    return a + b


add(5, 1)
