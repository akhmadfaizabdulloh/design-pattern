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
            string += "\nSaus terpasang:\n"
            
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
    def __str__(self):
        return "Daging"

class DoubleMeat:
    def __str__(self):
        return "Daging Double"

class Cheese:
    def __str__(self):
        return "Keju"

class Tomato:
    def __str__(self):
        return "Tomat"

class Lettuce:
    def __str__(self):
        return "Selada"

class Egg:
    def __str__(self):
        return "telur"