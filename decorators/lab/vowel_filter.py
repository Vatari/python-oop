def vowel_filter(function):
    def wrapper():
        res = function()
        filtered = [v for v in res if v.lower() in "aeiou"]
        return filtered

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
