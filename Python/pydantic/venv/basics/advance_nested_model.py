#advance nested models
from pydantic import BaseModel
from typing import Optional,List,Union

#1. optional nested models
class Address(BaseModel):
    street:str
    city:str
    postal_code:str

class Company(BaseModel):
    name:str
    address:Optional[Address] =None #this is optional nested model

class Employee(BaseModel):
    name:str
    company:Optional[Company]=None


#2.mixed data types
class TextContent(BaseModel):
    type:str='text' #type is string and we are calling it text
    content:str

class ImageContent(BaseModel):
    type:str="Image" #another type of syntax
    url:str
    alt_text:str

class Article(BaseModel):
    title:str
    sections:List[Union[TextContent,ImageContent]]

#3. deeply nested structure
class Country(BaseModel):
    name:str
    code:str

class State(BaseModel):
    name:str
    country:Country

class City(BaseModel):
    name:str
    state:State

class Address(BaseModel):
    street:str
    city:City
    postal_code:str

class Organization(BaseModel):
    name:str
    head_quarter=Address
    branches:List[Address]=[]