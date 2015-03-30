from libcpp.string cimport string
from libcpp.vector cimport vector

def page():
    
    cdef vector[string] content
    
    content.push_back("This thing all things devours:")
    content.push_back("Birds, beasts, trees, flowers;")
    content.push_back("Gnaws iron, bites steel;")
    content.push_back("Grinds hard stones to meal;")
    content.push_back("Slays king, ruins town,:)
    content.push_back("And beats high mountain down:)
    return content