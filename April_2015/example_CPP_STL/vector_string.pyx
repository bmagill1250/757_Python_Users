from libcpp.string cimport string
from libcpp.vector cimport vector

def page():
    
    cdef vector[string] content
    
    content.push_back("Three Rings for the elven kings")
    content.push_back("Seven for the dwarf lords")
    content.push_back("Nine for the mortal men")
    content.push_back("one for the dark lord")
    
    return content