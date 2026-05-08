#tuple
t1=(1,4,2,6,4,3,1)
#length of tuples
print("length: ",len(t1))
#count
print("count: ",t1.count(1))
#index
print("index: ",t1[4])
#concatenate
t2=(1,3)
t3=t1+t2
print("contenate:",t3)
#repeate 3 times
t4=(7,8)*3
print(t4)
#list to tuple
list=[2,4,3,6,5]
print(tuple(list))
#checking membership
print(1 in t1)
#sliceing
print("slice: ",t1[2:5])

#set
s1={1,2,3,4}
#add
s1.add(5)
print("after adding:",s1)
#remove
s1.remove(3)
print("after removeing: ",s1)
#set operations
s2={2,4,6}
s3={6,8,10}
print("union: ",s2|s3)
print("intersection: ",s2&s3)
print("difference: ",s2-s3)
#cheking membership
print(2 in s1)
#length
print("length: ",len(s1))
#clear
s1.clear()
print("clear: ",s1)