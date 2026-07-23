#create a decorator that times a function
import time
def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print("Execution time:",end-start,"seconds")
        return result
    return wrapper
@timer
def long_task():
    time.sleep(2)
    print("task completed")
long_task()