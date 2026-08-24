from pydantic import BaseModel,field_validator,model_validator

class User(BaseModel):
    username:str

    @field_validator('username')  #decorator
    def username_length(cls,v): #this is the class method that receives cls as the first parameter so the whole class is available to this
        if len(v)<4: #this v parameter is value validator
            raise ValueError("Username must be atleast 4 characters")
        return v

class SignupData(BaseModel):
    password:str
    confirm_password:str

    @model_validator(mode='after')#there are many modes this mode after means it runs after the field validation
    def password_match(cls,values): #since it is model validator it access all the values at the same time
        if values.password!=values.comfirm_password:
            raise ValueError("passwords do not match" )
        return values #important to write otherwise gives error


# Incoming data
#       ↓
# field_validator()
#       ↓
# Check / clean / transform
#       ↓
# return value
#       ↓
# Pydantic model