#Iterator Consumption

t=(10,20,30,40)
it=iter(t)
print("First iteration:")
for i in it:
    print(i)
print("Second iteration:")
for i in it:
    print(i)