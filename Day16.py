#list comprehension
#doubles the list
l=[num for num in range(1,11)]
print(l)
dl=[num*2 for num in l]
print(dl)
#only doubles the even numbers
l=[num for num in range(1,11)]
print(l)
dl=[num*2 for num in l if num%2==0]
print(dl)
#from a string only store a vpwels
word="engineering"
vowels=[words for words in word if words in "aeiou"]
print(vowels)
#create list of numbers divisible by 3 and 5 from 1 to 50
num=[n for n in range(1,51)]
div=[x for x in num if x%3==0 and x%5==0]
print(div)