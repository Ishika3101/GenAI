from pydantic import BaseModel,ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street:str
    city:str
    zip_code:str

class User(BaseModel):
    id:int
    name:str
    email:str
    is_active:bool=True
    createdAt:datetime
    address:Address
    tags:List[str]=[]

#whenever we mark anything with datetime it creates a problem as it is not compatible with pydantic model
#so we will config or customize it
    model_config=ConfigDict(
        #strf- string format time (small m -month and capital M-minute)
        json_encoders={datetime:lambda v:v.strftime('%d-%m-%Y %H:%M:%S')} #json-encoders encodes the string in the format we want
    )

user=User(
    id=1,
    name='ishika',
    email='goyal.ishika@gmail.com',
    createdAt=datetime(2025,12,14,15,30),
    address=Address(
        street='sec 73',
        city='ggn',
        zip_code='122004'
    ),
    is_active=False,
    tags=['premium']
)

python_dict= user.model_dump() #model_dump converts into dict
print(python_dict)

#converts everything into json string
json_str=user.model_dump_json()
print('='*30)
print(json_str)