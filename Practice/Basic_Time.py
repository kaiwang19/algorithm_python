"""
Common use of [time]
Authored by Kai Wang.
2020-04-19
"""

import time


def run():
    start = time.time()
    for i in range(1000):
        j = i * 2
        for k in range(j):
            t = k
            print(t)
    end = time.time()
    print('Program Execution Time: ', end - start)


def run2():
    start = time.process_time()
    for i in range(1000):
        j = i * 2
        for k in range(j):
            t = k
    end = time.process_time()
    print('CPU Execution Time: ', end - start)


# after Python Version 3.7
time.perf_counter_ns()
time.process_time_ns()
time.time_ns()

