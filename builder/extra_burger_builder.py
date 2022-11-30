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