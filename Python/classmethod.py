class Chai:
    def __init__(self,tea_type,sweetness,size):
        self.tea_type=tea_type
        self.sweetness=sweetness
        self.size=size

    @classmethod
    def from_dict(cls,order_data):
        return cls(order_data["tea_type"],
                   order_data["sweetness"],
                   order_data["size"])

    @classmethod
    def from_string(cls,order_string):
        tea_type,sweetness,size=order_string.split("-")
        return cls(tea_type,sweetness,size
        )
order1=Chai.from_dict({"tea_type":"masala","sweetness":"low","size":"200ml"}) #when we will print it will say i am object of chai
print(order1.__dict__)
print(order1) #<__main__.Chai object at 0x000001AD22209250>
order2=Chai.from_string("ginger-low-small")
print(order2.__dict__)
