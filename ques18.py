# Write a Python program to reverse a number using while loop.
a=int(input("enter the no. "))
rev=0
while(a!=0):
    r=a%10
    rev=r+rev*10
    a=a//10

print(rev)
