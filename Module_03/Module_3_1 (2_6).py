def mutual_inclusion(one, two):
    one_lower = str(one).lower()
    two_lower = str(two).lower()
    if two_lower in one_lower or one_lower in two_lower:
        return True
    else:
        return False

def single_root_words(root_word, *other_words):
    same_words = []
    for other_word in other_words:
        if mutual_inclusion(root_word, other_word):
            same_words.append(other_word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
