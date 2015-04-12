import numpy as np
#
#   Borrowed From "Numba vs. Cython, Take 2," Jake Vandeplas, 2013,  
#   https://jakevdp.github.io/blog/2013/06/15/numba-vs-cython-take-2/
#

def pairwise_numpy(X):
    
    return np.sqrt(( (X[:, None, :] - X) ** 2).sum(-1) )