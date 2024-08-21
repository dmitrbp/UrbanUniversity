def all_variants(text):
    text_len = len(text)
    for i in range(1, text_len + 1):
        for j in range(text_len):
            if j + i <= text_len:
                yield text[j: j + i]


a = all_variants('abc')
for element in a:
    print(element)
