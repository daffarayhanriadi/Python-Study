'''
abstract class adalah blueprint untuk class,
setiap class yang menginherit abstract class, 
harus mengimplementasikan method yang ada di dalam abstract class,
jika tidak, maka akan mengalami error
'''
# abc = abstract base class
from abc import ABC, abstractmethod

class Button(ABC): # Class Abstract
    
    @abstractmethod
    def click(self):
        pass
        # print("button click")
        
class PushButton(Button):
    
    def click(self):
        print("push button click")
        
class RadioButton(Button):
    
    def click(self):
        print("radio button click")
        
tombol1 = PushButton()
tombol1.click()
help(tombol1)

"""
Output:

push button click
Help on PushButton in module __main__ object:

class PushButton(Button)
 |  Method resolution order:
 |      PushButton
 |      Button
 |      abc.ABC
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  click(self)
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __abstractmethods__ = frozenset()
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Button:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)

"""