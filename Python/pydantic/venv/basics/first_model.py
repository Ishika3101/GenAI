from pydantic import BaseModel

class User(BaseModel):  #when we want to use pydantic powers we will inherit the basemodel class
    id:int
    name:str
    is_active:bool

input_data={'id':101,'name':"ishika",'is_active':True} #if we change any data type and it is different from the above pydantic class then it will throw pydantic/validation error



user=User(**input_data) #simply writing input_data is not a valid syntax ** used to unpack dictionary 
print(user)

#1.import Basemodel
#2. Type annotation
#3. model initialisation(always unpack the dict)
#4. automatic validation