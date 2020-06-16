## в два потока
import time
from threading import Thread


def countup(N):
    n = 0
    while n < N:
        n += 1


if __name__ == '__main__':
    max_for_thread = 30000000//2
    first_thread = Thread(target=countup, args=(max_for_thread,))
    second_thread = Thread(target=countup, args=(max_for_thread,))
    st_time = time.time()
    first_thread.start()
    second_thread.start()
    first_thread.join()
    second_thread.join()
    end_time = time.time()

    print(f'Время выполнения: {end_time-st_time}')