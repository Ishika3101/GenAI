from pydantic import BaseModel,computed_field,Field

class Product(BaseModel):
    price:float
    quantity:int

    @computed_field #this decorator marks the field as computed that means it will be calculated on the go
    @property #property decorator makes this accessible as an attribute
    def total_price(self) -> float:
        return self.price * self.quantity

class Booking(BaseModel):
    user_id:int
    room_id:int
    nights:int=Field(...,ge=1)
    rate_per_night=float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights*self.rate_per_night

booking=Booking(
    user_id=123,
    room_id=456,
    nights=1,
    rate_per_night=100.0
)

print(booking.total_amount) #dont access it like this totalamount() as it is a property not a method
print(booking.model_dump())# it gives whole model dump whats going on in the model