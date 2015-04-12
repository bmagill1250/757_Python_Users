from libcpp.string cimport string
from libcpp.vector cimport vector

cdef extern from "<algorithm>" namespace "std":
    void std_sort "std::sort" [iter](iter first, iter last)
    
def page():
    
    cdef vector[string] content
    
    content.push_back("He took his vorpal sword in hand:")
    content.push_back("Long time the manxome foe he sought --")
    content.push_back("So rested he by the Tumtum tree,")
    content.push_back("And stood a while in thought.")
    content.push_back(" ")
    content.push_back("One two! One two! And through and through")
    content.push_back("The vorpal blade went snicker-snack!")
    content.push_back("He left it dead, and with its head")
    content.push_back("He went galumphing back.")

    return content


def sort_list(list inList):
    
    cdef vector[string] output = inList
    std_sort[vector[string].iterator](output.begin(), output.end())
    
    return output
