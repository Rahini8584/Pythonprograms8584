#  Write a Python program to check whether a given year is a leap year.
a=int(input("enter the year"))
b=a%100
if(b%4==0):
    print(f"{a} is a leap year")
else:
    print(f"{a} is  not a leap year")
