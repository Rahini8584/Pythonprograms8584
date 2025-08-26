#print first 10 natural no. 
#for i in range(1,11):
  #  print(i)



#printing the multiplication table 
#a=int(input("enter the no."))
#for i in range(1,11):
 #   print((f"{a}*{i}={a*i}"))


#print all even no. from 1 to 100
#for i in range(1,101):
 #   if(i%2==0):
  #      print(i)


#find the factorial of the no. 
#a=int(input('enter no. '))
#f=1
#for i in range(1,a+1):
 #   f=f*i
#print(f)


#print the sum of first n natural no. 
  #  n=int(input('enter no. of terms '))
   # s=0
    #while(n!=0):
     #   s=s+n
      #  n-=1
   # print(s)

# print square of no. from 1 to 10 
#for i in range(1,11):
#    print(i**2)

#print the rev  counting 
#   n=int(input('enter the no. '))
 #   for i in range(n,0,-1):
  #      print(i)


#count the digits in given no. 
#  n=int(input('enter the no. '))
 # c=0
  #while(n!=0):
   #   n=n//10
    #  c=c+1
  #print(c)

#fabonacii series 
n=int(input('enter no. of terms '))
a=0
b=1
print("fibonacii series")
for i in range(1,n+1):
    print(a)
    a,b=b,a+b
    
