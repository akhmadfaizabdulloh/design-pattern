from classic_burger_builder import ClassicBurgerBuilder
from extra_burger_builder import ExtraBurgerBuilder

builder = ClassicBurgerBuilder()
builder.build_burger()
print(builder.get_product())

builder = ExtraBurgerBuilder() 
builder.build_burger() 
print(builder.get_product())