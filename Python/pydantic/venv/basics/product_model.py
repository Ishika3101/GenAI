from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str
    price:float
    in_stock:bool=True  #if pass on value then that value otherwise default value would be true

product_one=Product(id=1,name='laptop',price=999.99,in_stock=True)
product_two=Product(id=2,name='mouse',price=999.99) #no error
product_three=Product(name="phone")  #missing error

#pydantic tries to convert
#'123'=123  string to int
#"true"=true string to bool