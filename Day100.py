#Reverse string Iterator

class Reversestring: 
    def __init__(self,text):
        self.text=text
        self.index=len(text)-1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>=0:
            ch=self.text[self.index]
            self.index-=1
            return ch
        else:
            raise StopIteration
obj=Reversestring("python")
for ch in obj:
    print(ch)