#count frequency of list elements
n=[1,2,2,3,1,4,2]
freq={}
for i in n:
    if i in freq:
        freq[i] += 1
    else:
        freq[i]=1
print(freq)