# Student Marks Manager
# Description: Store each student's marks for 3 subjects in a dictionary using the student name as key
# and a tuple of marks as value. Calculate and print total and average marks for each student.
# Input Format: First line: integer N (number of students)
# Next N lines: student_name followed by 3 integers (marks)
# Output Format: {student_name: (total_marks, average_marks)}
# Sample Input:
# 2
# Ali 85 90 80
# Sara 75 88 92
# Sample Output:
# {'Ali': (255, 85.0), 'Sara': (255, 85.0)}
# Hint: Use tuple to store marks. Calculate total=sum(marks) and average=total/3

# n=int(input("enter the no. of students :"))
# sm={}
# for i in range(n):
#     data=input().split()
#     name=data[0]
#     marks=tuple(map(int,data[1:4]))
#     total=sum(marks)
#     avg=total/3
#     sm[name]=(total,avg)
# print(sm)

# 2. Product Sales Tracker
# Description: Store monthly sales of each product for 3 months in a dictionary with product name as
# key and a tuple of monthly sales as value. Print total sales for each product.
# Input Format: First line: integer N (number of products)
# Next N lines: product_name followed by 3 integers (monthly sales)
# Output Format: {product_name: total_sales}
# Sample Input:
# 2
# Laptop 50 60 55
# Mobile 100 120 110
# Sample Output:
# {'Laptop': 165, 'Mobile': 330}
# Hint: Use dict[name] = tuple_of_sales. Use sum(tuple_of_sales) for total

# n=int(input("enter no. of products : "))
# products={}
# for  i in range(n):
#     data=input().split()
#     prod=data[0]
#     sales=tuple(map(int,data[1:4]))
#     total=sum(sales)
#     products[prod]=(total)
# print(products)

# 3. Daily Steps Tracker
# Description: Track daily steps for each family member for 3 days in a dictionary. Print the total steps
# for each member.
# Input Format: First line: integer N (number of family members)
# Next N lines: name followed by 3 integers (steps per day)
# Output Format: {name: total_steps}
# Sample Input:
# 3
# John 5000 6000 5500
# Anna 7000 8000 7500
# Mike 4000 4500 5000
# Sample Output:
# {'John': 16500, 'Anna': 22500, 'Mike': 13500}
# Hint: Store daily steps in tuple and use sum() for total steps

# n=int(input("enter the no. of family members : "))
# tracker={}
# for i in range(n):
#     data=input().split()
#     name=data[0]
#     steps=tuple(map(int,data[1:4]))
#     total=sum(steps)
#     tracker[name]=(total)
# print(tracker)

# 4. Book Reading Tracker
# Description:  Track  number  of  pages  read  by  each  student  in  3  books  using  a  dictionary.  Print  the
# total pages read by each student.
# Input Format: First line: integer N (number of students)
# Next N lines: student_name followed by 3 integers (pages read)
# Output Format: {student_name: total_pages}
# Sample Input:
# 2
# Rahul 120 150 130
# Neha 200 180 170
# Sample Output:
# {'Rahul': 400, 'Neha': 550}
# Hint: Store pages read as tuple and use sum(tuple) for total pages.

# n=int(input("enter no. of students :"))
# tracker={}
# for i in range(n):
#     data=input().split()
#     name=data[0]
#     pages=tuple(map(int,data[1:4]))
#     total=sum(pages)
#     tracker[name]=(total)
# print(tracker)

# 5. Movie Ticket Sales
# Description:  Track  ticket  sales  of  different  movies  for  3  days  using  a  dictionary.  Print  total  tickets
# sold for each movie.
# Input Format: First line: integer N (number of movies)
# Next N lines: movie_name followed by 3 integers (tickets sold)
# Output Format: {movie_name: total_tickets}
# Sample Input:
# 3
# Avatar 100 120 110
# Titanic 90 80 95
# Inception 50 60 55
# Sample Output:
# {'Avatar': 330, 'Titanic': 265, 'Inception': 165}
# Hint: Store tickets as tuple and use sum(tuple) for total ticket

# n=int(input("enter the no. of movies :"))
# tracker={}
# for i in range(n):
#     data=input().split()
#     name=data[0]
#     sales=tuple(map(int,data[1:4]))
#     tickets=sum(sales)
#     tracker[name]=(tickets)
# print(tracker)