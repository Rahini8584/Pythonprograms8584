a=int(input())
b=int(input())
hcf=1
if(a>b):
    for i in range(1,b+1):
        if(a%i==0 and b%i==0):
            hcf=hcf*i
    print(hcf)

else:
    for i in range(1,a+1):
        if(a%i==0 and b%i==0):
            hcf=hcf*i
    print(hcf)