import functionE
import functionE_Cython

import numpy as np
import time

D = 5
N = 1500
X = np.array([np.random.rand(N) for d in range(D)]).T
beta = np.random.rand(N)
theta = 10

start = time.time()
functionE.rbf_network(X, beta, theta)

total_time = time.time() -start

start = time.time()
functionE_Cython.rbf_network(X, beta, theta)
cy_total_time = time.time() -start

speedUp = round(total_time/cy_total_time, 3)

print("Tiempo en python: {} \n".format(total_time))
print("Tiempo en cython: {} \n".format(cy_total_time))
print("speedUp: {} \n".format(speedUp))
