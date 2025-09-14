#  Write a Python program to print a diamond pattern of *.
n=int(input("enter the rows"))
x=n/2
x=int(x)
for i in range(1,(x)+1):
    print(" "*((x)-i)+'*'*(2*i-1))
for i in range((x)-1,0,-1):
    print(" "*((x)-i)+'*'*(2*i-1))