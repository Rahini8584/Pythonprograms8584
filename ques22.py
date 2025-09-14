# Write a Python program to print an inverted half pyramid of *.
n=int(input("enter no. of rows"))
for i in range(n,0,-1):
    print(" "*(n-i)+'*'*(2*i-1))
