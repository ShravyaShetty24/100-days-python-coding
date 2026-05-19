#lambda function
square=lambda a: a*a
print(square(5))
add=lambda a , b: a+b
print(add(3,5))
#nested function
def outer(name):
    def greet():
        print("welcome",name)
    greet()
outer("shravya")
#calculator
def calculator(a,b):
    def add():
        print("add: ",a+b)
    def sub():
        print("sub: ",a-b)
    def mul():
        print("mul: ",a*b)
    def div():
        if b==0:
            print("divison by zero is not allowed")
        else:
            print("division: ",a/b)
    add()
    sub()
    mul()
    div()
calculator(2,4)

#variable length argument
def add(*a):
    print("sum: ",sum(a))
add(2,4,5,6)