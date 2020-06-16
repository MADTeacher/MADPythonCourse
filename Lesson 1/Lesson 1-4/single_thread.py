import time


def countup(N):
    n = 0
    while n < N:
        n += 1


if __name__ == '__main__':
    st_time = time.time()
    countup(30000000)
    end_time = time.time()

    print(f'Время выполнения: {end_time-st_time}')