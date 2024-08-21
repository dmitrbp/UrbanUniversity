from enum import Enum


class Finder(Enum):
    FIND = 1
    COUNT = 2


def str_replace(source, replace_list):
    for element in replace_list:
        source = source.replace(element, '' if len(element) == 1 else ' ')
    return source


class WordsFinder:
    for_replacement = [',', '.', '=', '!', '?', ';', ':', ' - ']

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            splited_list = []
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    splited_list += [s.lower() for s in str_replace(line, WordsFinder.for_replacement).split()]
            all_words[file_name] = splited_list
        return all_words

    def find(self, word):
        return self.__finder(word, Finder.FIND)

    def count(self, word):
        return self.__finder(word, Finder.COUNT)

    def __finder(self, word, find_type: Finder):
        result = {}
        for key, value in self.get_all_words().items():
            repetition = 0
            for index in range(len(value)):
                if word.lower() == value[index]:
                    if find_type == Finder.COUNT:
                        repetition += 1
                    elif find_type == Finder.FIND:
                        result[key] = index + 1
                        break
            if find_type == Finder.COUNT:
                result[key] = repetition
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
