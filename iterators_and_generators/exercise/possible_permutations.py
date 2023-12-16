def possible_permutations(lst: list):
    if len(lst) <= 1:
        yield lst
    else:
        for i in range(len(lst)):
            for perm in possible_permutations(lst[:i] + lst[i + 1:]):
                yield [lst[i]] + perm
