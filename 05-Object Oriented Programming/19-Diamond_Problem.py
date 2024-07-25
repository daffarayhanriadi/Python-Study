class A:
    def show(self):
        print("Ini adalah show_A")

class B(A):
    def show(self):
        print("Ini adalah show_B")

class C(A):
    def show(self):
        print("Ini adalah show_C")
        
class D(B, C):
    pass

objek = D()
objek.show()
help(objek)

"""
Output:

Ini adalah show_B
Help on D in module __main__ object:

class D(B, C)
 |  Method resolution order:
 |      D
 |      B
 |      C
 |      A
 |      builtins.object
 |
 |  Methods inherited from B:
 |
 |  show(self)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from A:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 
"""