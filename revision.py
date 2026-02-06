# for i in range(3):
#     for j in range(2):
#         print(i, j)
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(4))
# sum of list using recursion 
# def list_sum(num_list):
#     if(len(num_list)==1):
#         return num_list[0]
#     else:
#         return num_list[0]+ list_sum(num_list[1:])
# num_list=[1,2,3,4,5]
# print(f"the sum of all the elements in string is {list_sum(num_list)}")
#fibonacci series using recursion 
# def fibonacci(n):
#     if(n==1):
#         return 0
#     elif(n==2):
#         return 1 
#     else:
#         return fibonacci(n-1) +fibonacci(n-2)
# n=int(input("enter the no. of terms "))
# print(fibonacci(n))
# n=int(input("enter the no."))
# for i in range(n-1,-1,-1):
#     print(i, sep=" ")
# l=(-1*n)
# for i in range(l):
#     print(n ,sep=" " , end=" ")
#     n=n+1
#     if(n==0):
#         print(n)
#         break
# #CENTER() FUNCTION 
# s="hello"
# print(s.center(12,"-"))
#insert element in list
# num=[12,45,65,34]
# num.insert(0,33)
# # for i in range(len(num)):
# #     print(num[i])
# num.sort()
# for k in range(len(num)):
#     print(num[k])
# def second_largest(nums):
#     a=list(set(nums))
#     a.sort
#     print(a)
#     if len(a)<2:
#         return None
#     return a[-2]
# nums=[12,34,65,90,43,55,76,89,22]
# print(second_largest(nums))   
#extend function in list 
# num=[6,5,45,66,34,54,32,12]
# num.extend([1,2,4])
# print(num)
# n=int(input("enter no. of rows"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# result=[print([i,j,k]) for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if(i+j+k!=n)]
# print(result)
# #runner up score 
# n = int(input())
# arr = map(int, input().split())
# lst=list(arr)
# l=lst.sort()
# for i in l:
#     print(i)
#     break
# n = int(input())
# arr = map(int, input().split())
# lst=list(set((arr)))
# print(lst[(len(lst))-2])
# for _ in range(int(input())):
#     name=input()
#     score=int(input())
# scores=[]
# scores.append(score)
# print(score)
# def fibonacci(n):
#     if n<=0:
#         return 0
#     elif n==1:
#         return 1 
#     else:
#         return fibonacci(n-1)+ fibonacci(n-2)
# scores=list()
# for i in range(int(input())):
#     name = input()
#     score = float(input()) 
#     scores.append(score)
# print(scores)
# scores.remove(max(scores))
# print(scores)
# scores=list()
# for i in range(int(input())):
#     name = input()
#     score = float(input()) 
#     scores.insert(0,[name,score])
# # print(scores)
# for num in range(10, 14):
#    for i in range(2, num):
#          if num%i == 1:
#               print(num)
#               break
# c=0
# total=0
# avg=0
# while True:
#     marks=int(input())
#     q=input()
#     c=c+1
#     total+=marks
#     avg=total/c
#     if(q=="n"):
#         print(avg)
#         break
#     else:
#         continue
# s=input("enter the string of your choice")
# result=""
# for i in range(len(s)):
#     result+=s[i]*(i+1)
# print(result)
# n=int(input("enter the no. of rows : "))
# c=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(c , end=" ")
#         c+=1
#     print()
# for i in range(n):
#     for k in range(n-1,i):
#         print(n ,end=" ")
#     print()
# rows=4
# num=1
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print("",end="")
#     for k in range(i):
#         print(num,end=" ")
#         num+=1
#     print()
# num=rows-1
# for i in range(1,rows+1):
#     for j in range(rows-num):
#         print("",end="")
#     for k in range(num):
#         print(k-i+5,end=" ")
#     num-=1
#     print()

# names_list=[]
# scores_list=[]
# max_scores=[]
# n=int(input("enter no. of students :"))
# for i in range(n):
#     name=input("enter your name : ")
#     score=input("enter your score : ")
#     names_list.append(name)
#     scores_list.append(score)
#     paired=list(zip(names_list,scores_list))
# paired.remove(max(paired))




# records=[] 
# for _ in range(int(input())): 
#     name = input() 
#     score = float(input()) 
#     records.append([name,score])
#     second_lowest=sorted(set([i[1] for i in records]))
#     names_list=sorted([i[0] for i in records if i[1]==second_lowest]) 

# for i in names_list:
#     print(i)

print("hi")