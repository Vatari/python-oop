from math import sqrt


def get_primes(nums: list):
    for num in nums:
        if num < 2:
            continue
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            yield num
