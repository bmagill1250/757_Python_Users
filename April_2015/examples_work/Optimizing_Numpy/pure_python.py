#
#   Borrowed From "Numba vs. Cython, Take 2," Jake Vandeplas, 2013,  
#   https://jakevdp.github.io/blog/2013/06/15/numba-vs-cython-take-2/
    #

import numpy as np

def pairwise_python(X):
    
    M = X.shape[0]
    N = X.shape[1]
    
    D = np.empty((M, M), dtype=np.float)
    
    for i in range(M):
        
        for j in range(M):
            
            d = 0.0
            
            for k in range(N):
                
                tmp = X[i, k] - X[j, k]
                d += tmp * tmp
                
            D[i, j] = np.sqrt(d)
