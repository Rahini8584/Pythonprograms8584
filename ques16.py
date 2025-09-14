# Write a Python program to print Fibonacci series up to n terms.
n=int(input('enter no. of terms '))
a=0
b=1
print("fibonacii series")
for i in range(1,n+1):
    print(a)
    a,b=b,a+b