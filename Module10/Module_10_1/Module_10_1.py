from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


# sync write
time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_stop = datetime.now()
print(f'Работа потоков {time_stop - time_start}')

# async wtite
time_start = datetime.now()

# thread_first = Thread(target=write_words, args=(10, 'example5.txt'))
# thread_second = Thread(target=write_words, args=(30, 'example6.txt'))
# thread_third = Thread(target=write_words, args=(200, 'example7.txt'))
# thread_fourth = Thread(target=write_words, args=(100, 'example8.txt'))
#
# thread_first.start()
# thread_second.start()
# thread_third.start()
# thread_fourth.start()
#
# thread_first.join()
# thread_second.join()
# thread_third.join()
# thread_fourth.join()

threads = []
threads.append(Thread(target=write_words, args=(10, 'example5.txt')))
threads.append(Thread(target=write_words, args=(30, 'example6.txt')))
threads.append(Thread(target=write_words, args=(200, 'example7.txt')))
threads.append(Thread(target=write_words, args=(100, 'example8.txt')))
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

time_stop = datetime.now()
print(f'Работа потоков {time_stop - time_start}')
