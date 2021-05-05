# cython: language level = 3
# from math import exp
import numpy as np
cimport numpy as np

cdef extern from "math.h":
    double exp(double x) nogil
    double pow(double base, double exponente) nogil

def rbf_network(np.ndarray[np.double_t, ndim=2] X, np.ndarray[np.double_t, ndim=1] beta, int theta):

    cdef int N, D
    cdef double r
    cdef np.ndarray[np.double_t, ndim=1] Y

    N = X.shape[0]
    D = X.shape[1]
    Y = np.zeros(N)

    cdef int i
    cdef int j

    for i in range(N):
        for j in range(N):
            r = 0
            for d in range(D):
                r += pow((X[j, d] - X[i, d]), 2) 
            r = pow(r, 0.5)
            Y[i] += beta[j] * exp(-pow((r*theta),2))

    return Y
