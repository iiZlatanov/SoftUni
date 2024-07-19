def vowel_filter(function):
    VOWELS = "aeiou"

    def wrapper():
        return [ch for ch in function() if ch.lower() in VOWELS]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
