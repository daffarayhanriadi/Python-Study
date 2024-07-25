from abc import ABC, abstractmethod

class Button(ABC):
    
    def __init__(self, set_link):
        self.link = set_link
    
    @abstractmethod
    def click(self):
        pass
    
    @property
    @abstractmethod
    def link(self):
        pass
    
class PushButton(Button):
    
    def click(self): 
        print("Go to: {}".format(self.link)) #self.link disini mengambil yang ada di class PushButton bukan class Button
        
    # @link.setter
    @Button.link.setter
    def link(self, input):
        self.__link = input
    
    # tidak memerlukan "Button." lagi karena sudah di deklarasikan diatasnya
    @link.getter # karena sudah ada Button.link diatas, maka method ini tidak memerlukan hal tersebut kembali
    def link(self):
        return self.__link
        
tombol1 = PushButton("www.kelasterbuka.id")

tombol1.click()

"""
Output:

Go to: www.kelasterbuka.id

"""