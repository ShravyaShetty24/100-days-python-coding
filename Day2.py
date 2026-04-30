#even numbers
def is_even():
    n=int(input("Enter the number:"))
    if(n%2==0):
        return True
    else:
        return False
#prime numbers
def is_prime():
    n=int(input("enter the number:"))
    flag=0
    for i in range(2,n):
        if(n%i==0):
            flag=1
    if(flag==1):
        return False
    else:
        return True
#main function
def main():
    print("Even:",is_even())
    print("Prime:",is_prime())
main()