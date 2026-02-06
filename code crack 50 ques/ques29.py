# Write a Python function to check whether a string is palindrome
def palindrome(a):
    a=a.lower()
    for i in range(len(a)-1):
        b=a[::-1]
    if(b==a):
        print("the string is palindrome.")

    else:
        print("the strin is not palindrome.")

a=input("enter a string : ")
palindrome(a)