import itertools
from icecream import ic
import timeit
import time

a = time.perf_counter()
time.sleep(1.5)
b = time.perf_counter()
print(">> A:", a)
print(">> B:", b)
print(b-a)

