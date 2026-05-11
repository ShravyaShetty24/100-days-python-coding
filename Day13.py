#program to input a number N and print numbers from 1 to N using while loop
n=int(input("Enter the number:"))
i=1
while i<=n:
    print(i)
    i+=1

#sum of digits
n=int(input("Enter the number: "))
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
print("sum: ",sum)

#Reverse a number
n=int(input("Enter the number: "))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("Reverse: ",rev)