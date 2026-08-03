def chai_customer():
    print("Welcome! What is your order?")
    order=yield
    while True:
        print(f"Preparing:{order}")
        order=yield

stall=chai_customer()
next(stall) #this line just start the generator so prints 2nd line
stall.send("Masala chai") #this passes value and run loop then 6th line pauses loop and waits for next value