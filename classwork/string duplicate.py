# def find_duplicate(s):
#     seen=set()
#     for ch in s:
#         if ch in seen:
#             return ch 
#         seen.add(ch)
#     return None
# user=input("enter  your name :")
# duplicate=find_duplicate(user)
# if duplicate:
#     print(f"duplicate character found :{duplicate}")
# else:
#     print("no duplicate found")

from collections import Counter
def find_all_duplicates(s):
    freq=Counter(s);
    duplicates={ch:count for ch , count in freq.items() if count>1 }
    return duplicates;
user=input("enter your name : ")
duplicates=find_all_duplicates(user)
if duplicates:
    print("duplicate character with count :")
    for ch , count in duplicates.items():
        print(f" '{ch}' ...{count} times")
else:
    print("no duplicate character  found ")