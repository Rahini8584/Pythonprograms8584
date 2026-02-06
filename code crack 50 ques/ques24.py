# Write a Python program to print Floyd’s triangle.
n=int(input("enter no. of rows "))
a=1
for i in range(1,n+1):
    for j in range(i):
        print(a,end=" ")
        a+=1
    print()