# numbers=[1,2,3,4,5,6,7,8,9]
# odd_numbers=list(filter(lambda x : x%2!=0,numbers ))
# print("the odd numbers are :", odd_numbers)

from functools import reduce 
numbers=[1,2,3,4]
prod=reduce(lambda x , y : x*y, numbers)
print("product of list elements are: " , prod )