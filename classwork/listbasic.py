# A LIST IN PYTHON IS ORDERED , MUTABLE, AND INDEXED COLLECTION THAT ALLOWS DUPLICATES . 
# IT IS WRITTEN IN SQUARE BRACKETS . 
# CAN STORE HETEROGENEOUS TYPE OF DATA TYPE . 
# my_list =[10, 20, 39,48, "list"]
# print(my_list)
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(len(my_list))
# my_list.insert(2,44)
# print(my_list)
# my_list.append("fuctions")
# print(my_list)

# #insert()- used to add element  at specific index 
l1=[10,20,30,40,50]
l1.insert(2,90)
print(l1)
l1.insert(3,[25,28,27])
print(l1)
nums=[1,4,6,0,33,18,43,22]
nums.sort()
print(nums)

# #using slicing
# l1=[10,20,30,40]
# print(l1[1:3])
# print(l1[-1]) 

# def second_largest(nums):
#     a=list(set(nums))
#     a.sort()
#     if len(a)<2:
#         return None
#     return a[-2]
# nums=[12,34,65,90,43,55,76,89,22]
# print(second_largest(nums))

# def reverse_list(rl):
#     return rl[::-1]
# rl=[12,23,5,3,7]
# print(reverse_list(rl))

# # extend() - used to add items at the end of the list by extending the list
# l1=[10,20,30,40,50]
# l1.extend([70,60,80])
# print(l1)

# def findpairs(nums,target):
#     pairs=[]
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if(nums[i]+nums[j]==target):
#                 pairs.append((nums[i],nums[j]))
#     return pairs

# nums=[1,5,-1,7,5]
# target=6
# print(findpairs(nums,target))