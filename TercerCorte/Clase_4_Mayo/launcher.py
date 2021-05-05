import time
from functionE_2 import *
import numpy as np

X = -1 + 2 * np.random.rand(200000000)

start = time.time()

array_f(X)

total_time = time.time() - start

start = time.time()

c_array_f(X)

cy_total_time = time.time() - start

start = time.time()

c_array_f_multi(X)

cy_multi_total_time = time.time() - start

speedUp = round(total_time/cy_total_time, 3)
speedUp_multi = round(total_time/cy_multi_total_time, 3)

print("Python time: {} \n".format(total_time))
print("Cython time: {} \n".format(cy_total_time))
print("Cython_multi time: {} \n".format(cy_multi_total_time))
print("SpeedUp: {} \n".format(speedUp))