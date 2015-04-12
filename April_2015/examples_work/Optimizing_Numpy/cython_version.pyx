import numpy as np
cimport cython
from libc.math cimport sqrt
#
#   Borrowed From "Numba vs. Cython, Take 2," Jake Vandeplas, 2013,  
#   https://jakevdp.github.io/blog/2013/06/15/numba-vs-cython-take-2/
#
@cython.boundscheck(False)
@cython.wraparound(False)

def pairwise_cython(double[:, ::1] X):
    
    cdef int M = X.shape[0]
    cdef int N = X.shape[1]
    cdef double tmp, d
    cdef double[:, ::1] D = np.empty((M,M), dtype=np.float64)
    
    for i in range(M):
        
        for j in range(M):
            
            d = 0.0
            
            for k in range(N):
                
                tmp = X[i, k] - X[j, k]
                d += tmp * tmp
                
            D[i, j] = sqrt(d)