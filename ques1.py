# Write a Python program to swap two numbers without using a third variable.
a=float(input("enter the first no. "))
b=float(input("enter the second no. "))
print("before swapping, first no. is ",a ,"and second no. is ",b,)
a=a+b
b=a-b
a=a-b
print("after swapping, the first no. is ",a," and second no. is ",b)
