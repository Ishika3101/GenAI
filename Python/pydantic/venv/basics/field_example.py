from pydantic import BaseModel
from typing import List,Dict,Optional

class Cart(BaseModel):
    user_id:int
    items:List[str]
    quantities:Dict[str,int]  #dict with the string keys and integer values

class BlogPost(BaseModel):
    title:str
    content:str
    image_url:Optional[str]=None #field which can be string or none

cart_data={
    "user_id":123,
    'items':['laptop','mouse','keyboard'],
    'quantities':{"laptop":1,"mouse":2,"keyboard":3}
}

cart=Cart(**cart_data)
