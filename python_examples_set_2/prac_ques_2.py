def prime(n):
    if n<2:
        return False
    if(n==2):
        return True
    if n%2==0:
        return False 
    for i in range(3,n+1,2):
        if(i>1 and n%i==0):
            return False
    return True 
nums=list(map( )
print(prime(nums))