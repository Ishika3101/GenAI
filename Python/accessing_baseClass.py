# 3 methods
#code duplication
class Chai:
    def __init__(self,type_,strength):
        self.type=type_
        self.strength=strength

class Ginger(Chai):
    def __init__(self,type_,strength,spice):
            self.type=type_
            self.strength=strength
            self.spice=spice

#explicitly call
    def __init__(self,type_,strength,spice):
         Chai.__init__(self,type_,strength)
         self.spice=spice

#super method
    def __init__(self, type_,strength,spice):
         super().__init__(type_,strength)
         self.spice=spice