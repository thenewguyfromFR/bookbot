def get_num_words (file_contents):
    return len(file_contents.split())


def get_list_char(file_contents):
    list_char = {}

    for c in file_contents:
        c = c.lower()

        if c in list_char:
            list_char[c] += 1
        else:
            list_char[c] = 1

    return list_char


def sort_on(items):
    return items["num"]


def get_sorted_char(list_char):
    sorted_char=[]

    for k in list_char:
        if k.isalpha():
            dict_char = {}
            dict_char["char"] = k
            dict_char["num"] = list_char[k]
            sorted_char.append(dict_char)

    sorted_char.sort(reverse=True, key=sort_on)

    return sorted_char
