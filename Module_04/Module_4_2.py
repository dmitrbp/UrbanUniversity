calls = 0


def count_calls():
    # ----- Variant 1 ------
    # global calls
    # calls += 1
    # ----- Variant 2 ------
    globals()['calls'] += 1


def string_info(string: str):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string: str, list_to_search: list):
    count_calls()
    # ----- Variant 1 ------
    return len(list(filter(lambda x: x.lower() == string.lower(), list_to_search))) > 0
    # ----- Variant 2 ------
    # for item in list_to_search:
    #     if item.lower() == string.lower():
    #         return True
    # return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic']))  # No matches
print(calls)
