# Write a Python program to display a simple calculator using match-case statement.

while True:
    print("choose the given operations + , - ,* , / , %,")
    print("press # to exit")
    a=input()

    if(a=="#"):
        break


    elif(a=='+'):
        x=int(input("enter the first no. "))
        y=int(input("enter the second no."))
        print("the sum is ",x+y)

    elif(a=="-"):
        x=int(input("enter the first no. "))
        y=int(input("enter the second no."))
        print(" the difference is " ,x-y)

    elif(a=="*"):
        x=int(input("enter the first no. "))
        y=int(input("enter the second no."))
        
        print("the product is ",x*y)

    elif(a=="/"):
        x=float(input("enter the first no. "))
        y=float(input("enter the second no."))
        print("the quotient is " , x/y)

    elif(a=="%"):
        x=int(input("enter the first no. "))
        y=int(input("enter the second no."))
        print("the  remainder is ", x%y)


    else:
        print("invalid input")     