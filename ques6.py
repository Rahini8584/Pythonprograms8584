# Write a Python program to find the largest of three numbers.
a,b,c=input("enter three no.  use , to separate").split(",")
if(a>b and a>c ):
    print(a,"is the largest of all")
elif(b>a and b>c):
    print(b,"is the largest no. of all")
elif(c>a and c>b):
    print(c,"is largest of all")