# MODULE IN PYTHON 
# import math 
import random
# print(math.sqrt(25))
# print(math.pi) 
#print(random.randint(1,100))
names=["VIRAT KOHLI THE GOAT","rohit sharma"," mitchell starc","pat cummings","josh hazelwood","jos buttler","joe root","jasprit bumrah","hardik pandya","kuldeep yadav","shreyas iyer" ,"mohm. shami","mohm. siraj","ravidra jadeja","suryakumar yadav","dale styen","ABD","steve smith"]
print(random.choice(names))
print(len(names))
# lottery game
matched=0
winning_numbers=[random.randint(1,50) for i in range(5)]
your_numbers=[random.randint(1,50) for i in range(5)]
for n in your_numbers:
    if(n in winning_numbers):
        matched=+1
print("winning_numbers are :",winning_numbers)
print("your numbers are :",your_numbers)
print("matched :",matched)


   
