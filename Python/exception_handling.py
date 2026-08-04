#custom exception
class InvalidChaiError(Exception):
    pass

def bill(flavor,cups):
    menu={"masala":20,"ginger":30}
    try:
        if flavor not in menu:
            raise InvalidChaiError("chai not available") #own error
        if not isinstance(cups,int):  
            raise TypeError("no of cups must be an integer")
        total=menu[flavor]*cups
        print(f"your bill for {cups} cups {flavor} chai:{total}")
    except Exception as e: #we can print all exceptions using exception class
        print("Error:",e)
    finally:
        print("thank you")

bill("mint",2)
bill("masala","three")
bill("ginger",3)

    
