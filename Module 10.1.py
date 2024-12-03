from time import sleep, time
import threading


#Function part
def write_words(word_count, file_name):
    with open(file_name, 'a') as file:
        for i in range(1, word_count + 1):
            file.write(f'"Какое-то слово № {i}\n')
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

start_time = time()

res_1 = write_words(10, 'example1.txt')
res_2 = write_words(30, 'example2.txt')
res_3 = write_words(200, 'example3.txt')
res_4 = write_words(100, 'example4.txt')

end_time = time()

program_time = round(end_time - start_time, 2)
print(program_time)
#Threading part 
threads = [
    threading.Thread(target=write_words, args=(10, 'example5.txt')),
    threading.Thread(target=write_words, args=(30, 'example6.txt')),
    threading.Thread(target=write_words, args=(200, 'example7.txt')),
    threading.Thread(target=write_words, args=(100, 'example8.txt'))
]

start_time_thread = time()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()



end_time_thread = time()

thread_time = round(end_time_thread - start_time_thread, 2)
print(thread_time)