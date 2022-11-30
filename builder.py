#burger.py
class Burger:
    def __init__(self):
        self.classic = False
        self.extra = False
        self.sauce = [] 
        self.primary = []
    
    def __str__(self): 
        string = ""
        if self.classic:
            string += "Burger Classic \n"
        if self.extra:
            string += "Burger Extra\n"
            
        
        if self.primary:
            string + "Kebutuhan utama terpasang:\n"
            
        for item in self.primary:
            string += "- " + str(item) + "\n"
        
        if self.sauce:
            string + "\nSaus terpasang:\n"
            
        for item in self.sauce:
            string += "- " + str(item) + "\n"
        
        return string

class TomatoSauce:
    def __str__(self):
        return "Saus Tomat"

class ChillySauce:
    def __str__(self):
        return "Saus Pedas"

class Meat:
    def _str__(self):
        return "Daging"

class DoubleMeat:
    def __str__(self):
        return "Daging Double"

class Cheese:
    def __str__(self):
        return "Keju"

class Tomato:
    def ___str__(self):
        return "Tomat"

class Lettuce:
    def __str__(self):
        return "Selada"

class Egg:
    def __str__(self):
        return "telur"


#burger_builder.py
from abc import ABC, abstractmethod

class BurgerBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass
    
    @abstractmethod
    def build_burger(self):
        pass


#classic_burger_builder.py
from burger_builder import BurgerBuilder 
from burger import *

class ClassicBurgerBuilder(BurgerBuilder): 
    def __init__(self):
        self.burger = Burger()
    
    def reset(self):
        self.burger = Burger()
    
    def get_product(self): 
        return self.burgerT
        
    def build_burger(self):
        self.burger.classic = True
        self.burger.primary.append(Meat())
        self.burger.primary.append(Lettuce())
        self.burger.primary.append(Tomato())
        self.burger.sauce.append(TomatoSauce())
        self.burger.sauce.append(ChillySauce())


#extra_burger_builder.py
from burger_builder import BurgerBuilder
from burger import *

class ExtraBurgerBuilder(BurgerBuilder): 
    def __init__(self):
        self.burger = Burger()
    
    def reset(self):
        self.burger = Burger()
    
    def get_product(self):
        return self.burger
        
    def build_burger(self):
        self.burger.extra = True
        self.burger.primary.append(Meat())
        self.burger.primary.append(DoubleMeat())
        self.burger.primary.append(Lettuce())
        self.burger.primary.append(Tomato())
        self.burger.sauce.append(TomatoSauce())
        self.burger.sauce.append(ChillySauce())


#main.py
from classic_burger_builder import ClassicBurgerBuilder
from extra_burger_builder import ExtraBurgerBuilder

builder = ClassicBurgerBuilder()
builder.build_burger()
print(builder.get_product())

builder = ExtraBurgerBuilder() 
builder.build_burger() 
print(builder.get_product())