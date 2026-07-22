#create a decorater to Log Calls

from datetime import datetime
def log_func(func):
    def wrapper(*args,**kwargs):
        print(f"Function name:{func.__name__}")
        print(f"Called At :{datetime.now()}")
        return func(*args,**kwargs)
    return wrapper
@log_func
def add(a,b):
    return a+b
result=add(10,20)
print("Result:",result)