add = ', 54200 Kuala Lumpur, Wilayah Persekutuan Kuala Lumpur, Malaysia'
removal = {"(odd)": '', "(even)": ''}


def replace_all(text, dict):
    for i, j in dict.items():
        text = text.replace(i, j)
    return text


while True:
    user = input("")
    store = user.split('	')
    print(store[1], ',', replace_all(store[0], removal), add)

