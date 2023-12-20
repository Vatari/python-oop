def number_increment(nums):
    def increase():
        increased_nums = [n + 1 for n in nums]
        return increased_nums

    return increase()


print(number_increment([1, 2, 3]))
