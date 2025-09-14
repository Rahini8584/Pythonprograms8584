# Write a Python program to calculate factorial of a number using while loop.
n=int(input("enter the no. "))
fact=1
while(n!=0):
    fact=fact*n
    n-=1
print("the factorial is ",fact)