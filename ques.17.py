#  Write a Python program to find the sum of digits of a given number.
n=int(input("enter the no. "))
sum=0
while(n!=0):
    a=n%10
    sum=sum+a
    n=n//10

print(sum)
