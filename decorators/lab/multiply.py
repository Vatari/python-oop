def multiply(n):
    def decorator(function):
        def wrapper(num):
            result = function(num)
            return result * n

        return wrapper

    return decorator


@multiply(3)
def add_ten(num):
    return num + 10


print(add_ten(3))
