#custom Iterator class

class EvenNo:
    def __init__(self,n):
        self.n=n
        self.current=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<=self.n:
            value=self.current
            self.current+=2
            return value
        else:
            raise StopIteration
nums=EvenNo(10)
for i in nums:
    print(i)