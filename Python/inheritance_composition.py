class BaseChai:
    def __init__(self,type_): #type_ because type is reserved in python
        self.type=type_
    def prepare(self):
        print(f"Preparing {self.type} chai...")

# inheritance
class MasalaChai(BaseChai):
    def add_spices(self):
        print("adding ginger,cloves")

# composition
class ChaiShop:
    chai_cls=BaseChai #this is not object creation this chai_cls is variable and we are keeping reference of this base chai

    def __init__(self):
        self.chai=self.chai_cls("Regular") #here we are creating regular type of chai(object) and passing the reference to self.chai

    def serve(self):
            print(f"Serving {self.chai.type} chai in the shop") #now we can access basechai methods
            self.chai.prepare()

class FancyChaiShop(ChaiShop):#inheritance
    chai_cls=MasalaChai #composition    

shop=ChaiShop() #this is an object and now we can access anything
fancy=FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()
# Since FancyChaiShop doesn't have its own __init__(), it inherits ChaiShop's __init__()
# fancy (FancyChaiShop object)
# │
# └── chai  ─────► MasalaChai object
#                    │
#                    └── type = "Regular"
# So chai is an attribute (instance variable) that stores a MasalaChai object.
