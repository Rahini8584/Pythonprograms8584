# Write a Python program to find the GCD of two numbers.
a=int(input("enter the  first no. "))
b=int(input("enter the second no. "))
gcd=1
if(a>b):
    for i in range(1,b):
        if(a%i==0 and b%i==0):
            gcd=gcd*i

else:
    for i in range(1,a):
        if(a%i==0 and b%i==0):
            gcd=gcd*i

print(f"gdc of {a} and {b} is {gcd}")
