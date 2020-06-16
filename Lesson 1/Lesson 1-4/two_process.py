## 2 процесса
from multiprocessing import Pool
import time


def countup(N):
    n = 0
    while n < N:
        n += 1


if __name__ == '__main__':
    max_for_process = 30000000//2
    process_pool = Pool(processes=2)
    st_time = time.time()
    first_process = process_pool.apply_async(countup, [max_for_process])
    second_process = process_pool.apply_async(countup, [max_for_process])
    process_pool.close()
    process_pool.join()
    end_time = time.time()
    print(f'Время выполнения: {end_time-st_time}')