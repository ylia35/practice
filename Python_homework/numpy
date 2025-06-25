import array
import numpy as np
from collections import deque

from time import time
import random
np.set_printoptions(threshold=np.inf)
arrayAr = array.array('l',[])
listAr = []
def time_clock(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        value = func(*args, **kwargs)
        end_time = time()
        print(f'Время выполнения функции {end_time-start_time:0.10f} сек.')
        return value
    return wrapper
def array():
    for i in range(10000000):
        j = random.randint(1, 1000)
        listAr.append(j)
        arrayAr.append(j)
@time_clock
def avg_f(s):
    avg = sum(s) / len(s)
    return avg
@time_clock
def avg_n(s):
    a = np.mean(s)
    return a

array()
numpyAr = np.array(listAr)
dequeAr = deque(listAr)
print(avg_f(listAr), 'listAr')
print(avg_f(arrayAr), 'arrayAr')
print(avg_f(dequeAr), 'dequeAr')
print(avg_n(numpyAr), 'numpyAr')
