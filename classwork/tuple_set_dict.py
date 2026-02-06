# tuple , set , dictionary 

#tuple is ordered , immutable collection in python 
#elements  can be of diff data types 
# represented by ()
# t=("red", "balck",12,3.3,2)
# print(t)
# print(len(t))

#t1=(12,34,9.44, 3, 3 )
# print(max(t1))

# print(t1.count(3))

# print(t1.index(12))

# print("sum :",sum(t1))

# x=34
# print(x in t1)

# unique=tuple(set(t1))
# print(unique )


# A dictionary in python is a collection of key value pairs 
# it is used to store data in a way that allows fast retrevial based on keys. follows insertion order, mutable , no duplicates, indexing by keys, unordered 
student={
    "name":"neeraj",
    "age":58,
    "course":"AIFT"
}
# # print(student)
# print(student["name"])
# print(student.get("age"))
student["email"]="neeraj@gmail.com"
student["age"]=35
# print(student)
# # student.clear()
# student.pop("email")
# del student["course"]
# print(student)

# for key in student.keys():
#     print(key)

# for value in student.values():
#     print(value)

# for key , value in student.items():
#     print(key,":",value)  


# nums=[1,2,6,3,4,2,3]
# def freq_count(nums):
#     freq={}
#     for n in nums:
#         freq[n]=freq.get(n,0)+1
#     return freq
# print(freq_count(nums))

# marks={
#     "rahini":99,
#     "ojaswini":98,
#     "ribhav":96,
#     "lakshay":96}
# brilliant=max(marks,key=marks.get)
# print(brilliant,":",marks[brilliant])

# def freq_count(st):
#     freq={}
#     for char in st:
#         freq[char]=freq.get(char,0)+1
#     return freq
# st="programming"
# print(freq_count(st))

d1={
    "a1":2,
    "a2":5,
    "a3":3}
d2={
    "a1":5,
    "a4":9
}
d2.update(d1)
print(d2)  