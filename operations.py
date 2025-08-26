while True:
    print("choose the given operations + , - ,* , / , %,")
    print("press # to exit")
    a=input()

    if(a=="#"):
        break


    elif(a=='+'):
        x=int(input("enter the first no. "))
        y=int(input("enter the second no."))
        print(x+y)

    elif(a=="-"):
        x=int(input("enter the first no. "))
        y=int(input("enter the second no."))
        print(x-y)

    elif(a=="*"):
        x=int(input("enter the first no. "))
        y=int(input("enter the second no."))
        print(x*y)

    elif(a=="/"):
        x=int(input("enter the first no. "))
        y=int(input("enter the second no."))
        print(x/y)

    elif(a=="%"):
        x=int(input("enter the first no. "))
        y=int(input("enter the second no."))
        print(x%y)


    else:
        print("invalid input")

       
        