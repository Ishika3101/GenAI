from pydantic import field_validator,BaseModel,model_validator
from datetime import datetime

class Person(BaseModel):
    first_name:str
    last_name:str

    @field_validator('first_name','last_name')
    def names_must_be_capitalized(cls,v):
        if not v.istitle():
            raise ValueError('names must be capitalized')
        return v

class User(BaseModel):
    email:str

    @field_validator('email')
    def normalize_email(cls,v):
        return v.lower().strip()

#validations run before the model
class Product(BaseModel):
    price:str #$4.44 so we can covert this into float in the model itself

    @field_validator('price',mode='before')
    def parse_price(cls,v):
        if isinstance(v,str): #isinstance() in Python is used to check whether an object belongs to a particular class or data type.
            return float(v.replace('$','')) #typecast to float
        return v


class DateRange(BaseModel):
    start_date:datetime
    end_date:datetime

    @model_validator(mode='after')
    def validate_date_range(cls,values): #values cause we will get all the values as we have taken the mode after
        if values.start_date>=values.end_date:
            raise ValueError("end date should be after start date")
        return values


