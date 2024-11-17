import time  # Импорты необходимых модулей и функций
from time import sleep
from threading import Thread

time_start = time.time() # Взятие текущего времени

def wite_words(word_count, file_name): # Объявление функции write_words
    with open(file_name, "w") as file:
        for i in range(word_count): # Запуск функций с аргументами из задачи
            file.write(f'Какое-то слово № {i + 1}\n')
            sleep(0.1) #файл с прерыванием после записи каждого на 0.1 секунду
    print(f'Завершилась запись в файл {file_name}')

wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time_end = time.time() # Взятие текущего времени
print(f'Работа потоков {time_end - time_start}') # Вывод разницы начала и конца работы функций
print()

time_start = time.time() # Взятие текущего времени

thread_a = Thread(target=wite_words, args=(10, 'example5.txt'))
thread_b = Thread(target=wite_words, args=(30, 'example6.txt'))
thread_c = Thread(target=wite_words, args=(200, 'example7.txt'))
thread_d = Thread(target=wite_words, args=(100, 'example8.txt'))

thread_a.start()
thread_b.start()
thread_c.start()
thread_d.start()

thread_a.join()
thread_b.join()
thread_c.join()
thread_d.join()

time_end = time.time() # Взятие текущего времени
print(f'Работа потоков {time_end - time_start}')