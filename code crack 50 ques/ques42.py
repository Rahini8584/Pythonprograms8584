# Write a Python program to check whether a list is palindrome.
def palindrome(s):
    result=""
    result=s[::-1]
    if(result==s):
        print(f"{s} is a palindrome string .") 
    else:
        print(f"{s} is not a palindrome string. ")

s=input("enter the string : ").lower()
palindrome(s)