#method overloading
class area:
    def calculate(self,a,b=None):
        if b is None:
            print("area of square:",a*a)
        else:
            print("area of rectangle:",a*b)
a=area()
a.calculate(5)
a.calculate(5,10)