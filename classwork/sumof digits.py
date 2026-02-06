n=int(input("enter the no."))
s=0
if(n!=0):
    while(n!=0):
        a=n%10
        s=s+a
        n=n//10
    print(f"the sum is {s}")

else:
    print(f"the sum is {n}")

n=int(input("enter the number :"))
total=0
while n>0:
    digit=n%10
    total+=digit
    n//=10
print("the sum of the digits of the number ",total)