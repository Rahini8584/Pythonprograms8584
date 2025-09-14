# Write a Python program to calculate grade of a student based on marks (if-elif ladder).
a=int(input("enter the marks "))
if(a>100 or a<0):
    print("invalid marks")
else:
    if(100>=a>=90):
        print("your grade is A+")

    elif(75<=a<90):
        print("your grade is A")

    elif(60<=a<75):
        print("your grade is  B")

    elif(40<=a<60):
        print("your grade is C")

    else:
        print("you are fail ")