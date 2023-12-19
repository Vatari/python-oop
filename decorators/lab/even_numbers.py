def even_numbers(function):
    def wrapper(nums):
        res = function(nums)
        return [n for n in res if n % 2 == 0]

    return wrapper


@even_numbers
def get_numbers(nums):
    return nums


print(get_numbers([1, 2, 3, 4, 5]))