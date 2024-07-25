# Method Resolution Order // Multiple Inheritance
'''
Method Resolution Order yang di inherit ke sebuah kelas 
itu tergantung dari urutan inheritance itu sendiri
'''

class A:
    
    def show(self):
        print("Ini adalah show_A")
        

class B:
    
    def show(self):
        print("Ini adalah show_B")
        
# class C(A, B)
class C(B, A):
    def show(self):
        print("Ini adalah show_C")

objek = C()
objek.show()
help(objek)

"""
Output:

Ini adalah show_C
Help on C in module __main__ object:

class C(B, A)
 |  # class C(A, B)
 |  
 |  Method resolution order:
 |      C
 |      B
 |      A
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  show(self)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from B:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 
"""