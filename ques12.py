# Write a Python program to check whether a number is divisible by 3 and 5.
a=input("enter a no.")
if(a%3==0 and a%5==0):
    print("the given no. is divisible by 3 and 5 both")

elif(a%3==0 and a%5!=0):
    print("the given no. is divisible by 3  but not by 5")

elif(a%3!=0 and a%5==0):
    print("the given no. is not divisible by 3 but by 5 ")

else:
    print("the given no. is neither divisible by 3 nor by 5 ")