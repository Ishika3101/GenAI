#decorators are used to wrap a function

from functools import wraps

def require_admin(func):
    @wraps(func) #preserve metadata and name of function
    def wrapper(user_role):
        if user_role!="admin":
            print("Access denied")
            return None #default return explicit return
        else:
            return func(user_role)
    return wrapper

@require_admin
def access_inventory(role):
    print("access")

access_inventory("user")
access_inventory("admin")