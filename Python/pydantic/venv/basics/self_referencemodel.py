from typing import List,Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id:int
    content:str
    replies:Optional[List['Comment']]=None #first of all comments are optional then if there then list of comment(type) and by default none

#whenever we are self-referencing we have to do this
Comment.model_rebuild() #this is known as forward references so in the forward references use the quote in the model name

#how to use it
comment=Comment(
    id=1,
    content="first comment",
    replies=[
        Comment(id=2,content='reply1'),
        Comment(id=3,content='reply2',replies=[Comment(id=4,content='nested reply')]),#nested inside this comment
    ]
)