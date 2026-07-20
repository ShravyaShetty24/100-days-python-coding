#Age verification:1.ask the user for their age
                #2.if age is valid,show in how many years will be 100 years old
                #3.handle invalid input gracefully

try:
    age=int(input("Enter your age:"))
    if age<0:
        print("age can not be negative")
    else:
        years=100-age
        if years>0:
            print(f"yor will be 100 years old in {years} years")
        elif years==0:
            print("your 100 years old!")
        else:
            print(f"you turned 100, {abs(years)} years ago")
except ValueError:
    print("invalid input! please enter a valid no.")