def words_sorting(*args):
    all_words_dict = {}
    for word in args:
        all_words_dict[word] = 0
        for ch in word:
            all_words_dict[word] += ord(ch)

    if sum(all_words_dict.values()) % 2 == 0:
        sorted_dict = sorted(all_words_dict.keys())
        result = ""
        for el in sorted_dict:
            result += f"{el} - {all_words_dict[el]}\n"

        return result

    else:
        sorted_dict = sorted(all_words_dict.items(), key=lambda x: -x[1])
        result = ""
        for el in sorted_dict:
            result += f"{el[0]} - {el[1]}\n"

        return result


print(words_sorting('escape', 'charm', 'mythology'))
print(words_sorting('escape','charm','eye'))
print(words_sorting('cacophony','accolade'))
