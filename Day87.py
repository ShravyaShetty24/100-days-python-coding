#Multiple Decorator

def line_decorator(func):
    def wrapper():
        print("=========")
        func()
        print("=========")
    return wrapper
def arow_decorator(func):
    def wrapper():
        print(">>>",end="")
        func()
    return wrapper
@line_decorator
@arow_decorator
def my_name():
    print("Shravya")
my_name()