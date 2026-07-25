#create a Decorator that only allows a specific User
def allow_only(func):
    def wrapper(name):
        if name=="admin":
            return func(name)
        else:
            print("Access Denied")
    return wrapper
@allow_only
def view_data(name):
    print("Welcome",name)
    print("Access Granted")
view_data("admin")
view_data("user")