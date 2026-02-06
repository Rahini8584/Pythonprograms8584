a=int(input("enter th no."))
if(a>=100 and a%5==0):
    print("the given no. is greater than or equal to 100 and divisible by 5 ")
else:
    if(a>100 and a%5!=0):
        print("the given no. is greater than 100 but  not divisible by 5 ")
    elif(a<100 and a%5==0):
        print("the given no.is not greater than 100 but divisible by 5")
    else:
        print("the given no. is neither greater than 100 nor the no. is divisible by 5")