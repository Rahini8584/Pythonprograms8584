# import math
# import random 
# def circle_area(radius):
#     return math.pi*(radius**2)
# def compound_amount(principal,rate=0.05 , time=1, n=1):
#     return principal*((1+rate/n)**(n*time))
# def factorial(n):
#     if n==0 or n==1 :
#         return 1 
#     else:
#         return n*factorial(n-1)
# def fibonacci(n):
#     if n<=0:
#         return 0
#     elif n==1:
#         return 1 
#     else:
#         return fibonacci(n-1)+ fibonacci(n-2) 
# numbers=[1,2,3,4,5,6]
# squares=list(map(lambda x: x**2 , numbers))
# evens=list(filter(lambda x: x%2==0,numbers))
# if __name__=="_main_":
#     print("circle area(r=5):",circle_area(5))
#     print("compound amount (p=1000 , r=0.05 , t=2):",compound_amount(1000,0.05,2))
#     # print("rolling a dice:",roll_dice())
#     print("factorial of 5 :", factorial(5))
#     print("fibonacci of 6",fibonacci(6))
#     print("original list:",numbers)
#     print("squares(map):",squares)
#     print("evens(filters):",evens
# grocery_list=[]
# priority_list=["rice","milk","curd","flour"]
# print("to add priority items to grocery list , enter pl")
# while True:
#     item=input("enter the grocery items :").lower()
#     grocery_list.append(item)
#     if item=="done":
#         grocery_list.remove("done")
#         break
#     elif(item=="pl"):
#         grocery_list.remove("pl")
#         grocery_list.extend(priority_list)
# grocery_list.sort()
# print(grocery_list)
# print(f"no. of items in grocery list are {len(grocery_list)}")
# def print_categories(categories):
#     print("/n---------- GROCERY CATEGORIES---------")
#     for category, 
# create a 2-D list for students marks , compute row -wise totals and averages  , column - wise averages , and generate the transpose of the list. Demonstrate indexing and transversal of 2-D structures
# step 1 
# marks=[
#     [85,90,45],
#     [45,78,63],
#     [77,84,72],
#     [80,90,70]
# ]
# print("original 2-D list (student marks):")
# for row in marks:
#     print(row)

# print("Row-wise totals and average :")
# for i in range(len(marks)):
#     row_total=sum(marks[i])
#     row_avg=row_total/len(marks[i])
#     print(f"student{i+1}: total={row_total},averages={row_avg:2f}")

# print("  column-wise Average ")
# num_rows=len(marks)
# num_cols=len(marks[0])
# for col in range(num_cols):
#     col_sum=0
#     for row in range(num_rows):
#         col_sum+=marks[row][col]
#     col_avg=col_sum/num_rows
#     print(f"subject{col+1}: Average ={col_avg:2f}")

# transpose=[]
# for col in range(num_cols):
#     new_row=[]
#     for row in range(num_rows):
#         new_row.append(marks[row][col])
#     transpose.append(new_row)

# print(" Transpose of the list")
# for row in transpose:
#     print(row)


# print( "Traversal using nested loops")
# for i in range(num_rows):
#     for j in range(num_cols):
#         print(f"marks[{i}{j}]={marks[i][j]}")



# create a 3-D list for student marks , compute row-wise totals and averages , column-wise averages , and generate the transpose of the list . demonstrate indexing and transversal of 2-D structues .
# marks=[
#     [
#     [78,80,98,74],
#     [89,88,72,95],
#     [90,93,95,92]
#     ],
#     [
#     [88,90,81,85],
#     [57,65,72,66],
#     [88,84,82,83]
#     ]
# ]
# for class_index, class_group in enumerate(marks):
#     print(f"\n ----Class{class_index + 1} : ---- ")
#     for studentindex , student_marks in enumerate(class_group):
#         total=sum(student_marks)
#         avg = total/len(student_marks)
#         print(f"student{studentindex + 1}  → Total = {total} , Average = {avg:.2f}")
# class1 = marks[0]
# num_students=len(class1)
# num_subjects=len(class1[0])
# print("\n-------    Subject-wise Averages (Class 1) :   ---------- ")
# for subject in range(num_subjects):
#     subject_total = 0
#     for student in range(num_students):
#         subject_total += class1[student][subject]
#     print(f"  Subject {subject + 1} Average = {subject_total / num_students:.2f}")
# transpose = []
# for col in range(num_subjects):        
#     new_row = []
#     for row in range(num_students):    
#         new_row.append(class1[row][col])
#     transpose.append(new_row)
# print("\n----  Transpose of  Class 1:   -------")
# for row in transpose:
#     print(row)
# print("\n-------   Indexing Examples:   --------")
# print("marks[0][1][2] =", marks[0][1][2])  
# print("marks[1][2][0] =", marks[1][2][0])

# print("\n------  2-D Traversal of Class 2:   ----------")
# for i in range(len(marks[1])):
#     for j in range(len(marks[1][i])):
#         print(marks[1][i][j], end=" ")
#     print()


# Text Analyzer
# Get user input
text = input("Enter a text to analyze: ")

print("\n--- Original Text ---")
print(text)

# Basic transformations
print("\n--- Transformations ---")
print("Capitalized:", text.capitalize())
print("Lowercase:", text.lower())
print("Uppercase:", text.upper())
print("Stripped (remove spaces at ends):", text.strip())

# Replace and count
old_word = input("\nEnter a word to replace: ")
new_word = input("Enter the new word: ")
replaced_text = text.replace(old_word, new_word)
print("After replacement:", replaced_text)

word_to_count = input("\nEnter a word to count occurrences: ")
print(f"'{word_to_count}' occurs {text.count(word_to_count)} times")

# Find and index
word_to_find = input("\nEnter a word to find: ")
position = text.find(word_to_find)
if position != -1:
    print(f"First occurrence of '{word_to_find}' is at index {position}")
else:
    print(f"'{word_to_find}' not found")

# Index raises an error if not found
try:
    idx = text.index(word_to_find)
    print(f"(Using index) '{word_to_find}' found at {idx}")
except ValueError:
    print(f"(Using index) '{word_to_find}' not found")

# Check start/end
print("\n--- Starts/Ends With ---")
print("Starts with 'Hello'? ->", text.startswith("Hello"))
print("Ends with '.'? ->", text.endswith("."))

# Split and analyze words
words = text.split()
print("\n--- Words in the text ---")
print(words)
print("Number of words:", len(words))

# Analyze each word
print("\n--- Word-wise analysis ---")
for w in words:
    print(f"'{w}': uppercase={w.upper()}, lowercase={w.lower()}, length={len(w)}")


# Employee Management code 
# Employee Management System (no classes, in-memory)
# Employee Management System (no classes, in-memory)

# employees = []   # each employee will be a dictionary

# def add_employee():
#     print("\n--- Add Employee ---")
#     emp_id = input("Enter ID: ")
#     # check if ID already exists
#     for emp in employees:
#         if emp["id"] == emp_id:
#             print("ID already exists. Try again.")
#             return
#     name = input("Enter Name: ")
#     age = input("Enter Age: ")
#     dept = input("Enter Department: ")
#     salary = input("Enter Salary: ")

#     employee = {
#         "id": emp_id,
#         "name": name,
#         "age": age,
#         "dept": dept,
#         "salary": salary
#     }
#     employees.append(employee)
#     print("Employee added successfully.")

# def show_all():
#     print("\n--- All Employees ---")
#     if not employees:
#         print("No employees found.")
#         return
#     for emp in employees:
#         print(f"ID: {emp['id']}, Name: {emp['name']}, Age: {emp['age']}, "
#               f"Dept: {emp['dept']}, Salary: {emp['salary']}")

# def search_employee():
#     print("\n--- Search Employee ---")
#     emp_id = input("Enter ID to search: ")
#     for emp in employees:
#         if emp["id"] == emp_id:
#             print(f"ID: {emp['id']}, Name: {emp['name']}, Age: {emp['age']}, "
#                   f"Dept: {emp['dept']}, Salary: {emp['salary']}")
#             return
#     print("Employee not found.")

# def update_employee():
#     print("\n--- Update Employee ---")
#     emp_id = input("Enter ID to update: ")
#     for emp in employees:
#         if emp["id"] == emp_id:
#             print("Leave blank if you don't want to change a field.")
#             new_name = input(f"New Name ({emp['name']}): ")
#             new_age = input(f"New Age ({emp['age']}): ")
#             new_dept = input(f"New Dept ({emp['dept']}): ")
#             new_salary = input(f"New Salary ({emp['salary']}): ")

#             if new_name:
#                 emp["name"] = new_name
#             if new_age:
#                 emp["age"] = new_age
#             if new_dept:
#                 emp["dept"] = new_dept
#             if new_salary:
#                 emp["salary"] = new_salary

#             print("Employee updated.")
#             return
#     print("Employee not found.")

# def delete_employee():
#     print("\n--- Delete Employee ---")
#     emp_id = input("Enter ID to delete: ")
#     for i, emp in enumerate(employees):
#         if emp["id"] == emp_id:
#             employees.pop(i)
#             print("Employee deleted.")
#             return
#     print("Employee not found.")

# def menu():
#     while True:
#         print("\n===== Employee Management =====")
#         print("1. Add Employee")
#         print("2. Show All Employees")
#         print("3. Search Employee by ID")
#         print("4. Update Employee")
#         print("5. Delete Employee")
#         print("6. Exit")

#         choice = input("Enter choice (1-6): ")

#         if choice == "1":
#             add_employee()
#         elif choice == "2":
#             show_all()
#         elif choice == "3":
#             search_employee()
#         elif choice == "4":
#             update_employee()
#         elif choice == "5":
#             delete_employee()
#         elif choice == "6":
#             print("Exiting program.")
#             break
#         else:
#             print("Invalid choice. Try again.")

# # start the program
# menu()

# from datetime import datetime
# # 1. Students list as tuples (immutable)
# students = ("Alice","Bob","Charlie","David","Eva")
# print("Students (immutable tuple):", students)

# # 2. Attendance records as a dictionary
# # key = date, value = set of present students
# attendance = {}

# # Function to mark attendance for today
# def mark_attendance(present_students):
#     today = datetime.today().date()  
# # get today's date
#     attendance[today] = set(present_students)
#     print(f"\nAttendance for {today} marked.")

# # Example: mark some students present
# mark_attendance(["Alice", "Charlie", "Eva"])

# # Another day
# mark_attendance(["Bob", "Charlie", "David"])

# # 3. View attendance records
# print("--- Attendance Records ---")
# for date, present in attendance.items():
#     print(f"{date}: {present}")

# # 4. Set operations
# print("\n--- Set Operations ---")
# dates = list(attendance.keys())
# if len(dates) >= 2:
#     day1 = attendance[dates[0]]
#     day2 = attendance[dates[1]]

#     print(f"Students present both days (intersection): {day1 & day2}")
#     print(f"Students present at least one day (union): {day1 | day2}")
#     print(f"Students absent on day 2 but present on day 1 (difference): {day1 - day2}")

# # 5. Dictionary methods
# print("\n--- Dictionary Methods ---")
# print("Dates recorded:", attendance.keys())
# print("Attendance values:", attendance.values())
# print("Items:", attendance.items())

# # Check if a specific student was present on a specific day
# check_date = dates[0]
# student_to_check = "Alice"
# was_present = student_to_check in attendance.get(check_date, set())
# print(f"\nWas {student_to_check} present on {check_date}? -> {was_present}")

# # 6. Adding a new student (tuple is immutable)
# print("\n--- Tuple Immutability ---")
# print("Original students:", students)
# # Tuples cannot be changed, but we can create a new tuple
# new_students = students + ("Frank",)
# print("Updated students (new tuple):", new_students)

# # 7. Summary
# print("\n--- Attendance Summary ---")
# for student in new_students:
#     present_days = sum(student in present for present in attendance.values())
#     print(f"{student}: Present {present_days} day(s)")

# import random

# # 1. Define quiz questions
# # Each question is a tuple: (question, [options], correct_answer_index)
# questions = [
#     ("What is the capital of France?", ["Paris", "London", "Berlin", "Rome"], 0),
#     ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Saturn"], 1),
#     ("What is 5 + 7?", ["10", "11", "12", "13"], 2),
#     ("Who wrote 'Hamlet'?", ["Mark Twain", "Charles Dickens", "William Shakespeare", "J.K. Rowling"], 2),
#     ("Which gas do plants absorb from the atmosphere?", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], 1)] 
# # 2. Shuffle questions
# random.shuffle(questions)
# # 3. Quiz logic
# score = 0
# for i, q in enumerate(questions, start=1):
#     question, options, correct_index = q
#     print(f"\nQuestion {i}: {question}")
#     for idx, option in enumerate(options, start=1):
#         print(f"  {idx}. {option}")
#     while True:
#         try:
#             answer = int(input("Your answer (1-4): "))
#             if 1 <= answer <= 4:
#                 break
#             else:
#                 print("Please enter a number between 1 and 4.")
#         except ValueError:
#             print("Invalid input. Enter a number between 1 and 4.")
#     if answer - 1 == correct_index:
#         print("Correct!")
#         score += 1
#     else:
#         print(f"Wrong! Correct answer: {options[correct_index]}")
# print(f"\nYour total score: {score}/{len(questions)}")