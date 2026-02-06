# Create a dictionary of students with marks . find average marks . 
students={
    "a":23,
    "b":99,
    "c":97,
    "d":78,
    "e":80
    }
def avg_marks(students):
    avg=0
    for value in students.values():
        avg=(avg+value)
    avg=avg/5    
    return(avg)
print("Average marks of 5 students are",avg_marks(students))
# Write a Python code to remove duplicate values from a dictionary
d1={
    "n":90,
    "k":55,
    "r":90,
    "e":54,
    "j":55
}
s1=set()
s2=set()
for value, key in d1.items():
    s1.add(value)
    s2.add(key)
print(s1,s2)
d2=zip(s1,s2)
print(dict(d2))

# Count words in a sentence using dictionary.
def count_words(sentence):
    count={}
    words=a.split()
    for word in words:
        count[word]=count.get(word,0)+1
    return count
a=" red blue pink  red yellow blue black pink"
print(count_words(a))
