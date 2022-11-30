from abc import ABC, abstractmethod

class BurgerBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass
    
    @abstractmethod
    def build_burger(self):
        pass