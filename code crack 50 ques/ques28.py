# Write a Python function to find the factorial of a number.
def fact(n):
    f=1
    for i in range(n):
        f=f*n
        n-=1
    return(f)
n=int(input("enter the number : "))
print(fact(n))