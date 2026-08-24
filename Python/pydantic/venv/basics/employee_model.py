from typing import Optional
from pydantic import BaseModel,Field
import re #regular expression

class Employee(BaseModel):
    id:int
    name:str=Field(  #now we can use field as a method or a class
        ...,  #it indicates a required field
        min_length=3,
        max_length=50,
        description="Employee name",
        examples="ishika"
    ) 
    department:Optional[str]='General'
    salary:float=Field(
        ...,
        ge=10000, #ge means salary should be greater than or equal to
        le=100000,
        description="annual salary"
    )

class User(BaseModel):
    email:str=Field(
        ...,
        regex=r''
    )
    phone:str=Field(...,regex=r'')
    discount:float=Field(
        ...,
        ge=0,
        le=100,
        description="discount percentage"
    )