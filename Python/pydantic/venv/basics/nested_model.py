from typing import List,Optional
from pydantic import BaseModel

class Address(BaseModel):
    street:str
    city:str
    postal_code:str

#the user contains reference of address model
class User(BaseModel):
    id:int
    name:str
    address:Address #address is type of address which is already defined above so this is nested
