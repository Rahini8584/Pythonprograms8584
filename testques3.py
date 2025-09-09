#Write a program that takes two numbers as input and prints their sum, difference, product, and
# division.
a=float(input("enter the first no."))
b=float(input("enter the second no."))
print("the sum of the numbers is ",a+b)
print("the difference of the  numbers. is ",a-b)
print("the product of the numbers is ",a*b)
print("the quotient is ",a/b)

#Write a program that prints 'Hello' five times but does nothing when the loop counter is 3 (use
# pass).
for i in range(6):
    if(i==3):
        pass
    else:
        print("hello")


#Write a program to compare two objects using 'is' and 'is not'.
a=44.00
b=44.01
print(a is b)
print(a is not b)       