cdef extern from "mt19937ar.h":
#
#   Declarations for C functions from random number generator
#    
    void init_genrand(unsigned long s)
    
    double genrand_real1()
  
def init_state(unsigned long s):
    "Initializes random number generator"
    
    init_genrand(s) 
   
def rand():
    "Retrieves random numbers"    
        
    return genrand_real1()