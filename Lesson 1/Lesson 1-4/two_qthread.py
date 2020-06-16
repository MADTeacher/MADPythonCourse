import sys
import time

VER_LIB = '!PyQt'

if VER_LIB == 'PyQt':
    from PyQt5.QtCore import QThread
else:
    from PySide2.QtCore import QThread


class TestQtThread(QThread):

    def __init__(self, n, parent=None):
        super(TestQtThread, self).__init__(parent)
        self.N = n

    def run(self):
        n = 0
        while n < self.N:
            n += 1


if __name__ == '__main__':
    max_for_thread = 30000000//2
    st_time = time.time()
    first_thread = TestQtThread(max_for_thread)
    second_thread = TestQtThread(max_for_thread)
    first_thread.start()
    second_thread.start()
    first_thread.wait()
    second_thread.wait()
    end_time = time.time()
    print(f'Время выполнения: {end_time - st_time}')

