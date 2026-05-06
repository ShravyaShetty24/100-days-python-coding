#exponential function
def raise_to_power():
    base_num=int(input("Enetr the base number: "))
    pow_num=int(input("Enter the power: "))
    result=1
    for i in range(pow_num):
        result=result*base_num
    return result
print(raise_to_power())