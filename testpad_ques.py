# number=int(input().strip())
# result=0
# temp=number
# c=0
# x=number
# while(temp!=0):
#     c+=1
#     temp=temp//10
# while(x!=0):
#     rem=x%10
#     result=result+rem**c
#     x=x//10
# if(number==result):
#     print(number,"is an armstrong no.")
# else:
#     print(number,"is not an armstrong no. ")
# def fib_sequence(n):
#     a=0
#     b=1
#     for i in range(n):
#         print(a)
#         a,b=b,a+b
# n=int(input())
# fib_sequence(n)
# x=int(input())
# y=int(input())
# print(min(x,y))
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# n=int(input())
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()
# n=int(input())
# for i in range(1,n+1):
#     c=i
#     for j in range(n,0,-1):
#         if(j>i):
#             print("*",end="")
#         else:
#             print(c,end="")
#             c-=1
#     print() 
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     for k in range(j-1,0,-1):
#         print(k,end="")
#     print()
# c=1
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(c,end=" ")
#         c+=1
#     print()
# n = int(input())
# current = 1
# for row in range(1, n + 1):
#     numbers = []
#     for col in range(row):
#         numbers.append(str(current))
#         current += 1
#     print(' '.join(numbers))
# def binaryToDecimal(binary):
#     temp=binary
#     l=0
#     while temp!=0:
#         temp//=10
#         l+=1
#     decimal=0
#     for i in range(l,-1,-1):
#         decimal+=((binary%10)*(2**i))
#         binary=binary//10
#     return decimal
# n=int(input())
# print(binaryToDecimal(n))
# def binaryToDecimal(binary):
#     binary=int(binary)
#     temp=binary
#     l=0
#     while temp!=0:
#         temp//=10
#         l+=1
#     decimal=0
#     for i in range(l,-1,-1):
#         decimal=decimal+(((binary)%10)*(2**i))
#         binary=binary//10
#     return decimal
# # n=input()

# # print(binaryToDecimal(n))
# def binaryToDecimal(binary):
#     decimal=0
#     for i in range(0,len(binary)):
#          decimal=decimal+((int(binary[i])*(2**i)))
#          print(decimal)
# n=input()
# binaryToDecimal(n)



# def evenDigits(n):
#     # Base case: n is 0 or negative
#     if n <= 0:
#         return 0
#     # Recursive case: process last digit
#     last_digit = n % 10
#     rest = evenDigits(n // 10)
    
#     # If last digit is even, add it to result
#     if last_digit % 2 == 0:
#         return rest * 10 + last_digit
#     else:
#         return rest

def binaryToDecimal(binary):
    number=int(binary)
    decimal=0
    n=0
    while number>0:
        decimal+=(2**n)*(number%10)
        number=number//10
        n+=1
    return decimal
n=int(input())
for i in range(n):
    binary=input()
    print(binaryToDecimal(binary))

# Q1 Village Festival Ingredient Mixer
# def ingredient_mixer(contributions):
#     #Type your code here
#     unique_items = set()

#     for group in contributions:
#         for item in group:
#             unique_items.add(item)

#     final_list = sorted(unique_items)

#     print(final_list)
#     print(len(final_list))

# n1=eval(input())
# ingredient_mixer(n1)





