# Write a Python program to check whether a number is prime.
n=int(input("enter the no."))
c=0
for i in range(1,n+1):
    if(n%i==0):
        c=c+1
    
if(c>=3):
    print("the given no. is not prime ")
else:
    print("the given no. is prime")