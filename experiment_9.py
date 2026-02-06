
from datetime import datetime
# 1. Students list as tuples (immutable)
students = ("Alice","Bob","Charlie","David","Eva")
print("Students (immutable tuple):", students)

# 2. Attendance records as a dictionary
# key = date, value = set of present students
attendance = {}

# Function to mark attendance for today
def mark_attendance(present_students):
    today = datetime.today().date()  
# get today's date
    attendance[today] = set(present_students)
    print(f"\nAttendance for {today} marked.")

# Example: mark some students present
mark_attendance(["Alice", "Charlie", "Eva"])

# Another day
mark_attendance(["Bob", "Charlie", "David"])

# 3. View attendance records
print("--- Attendance Records ---")
for date, present in attendance.items():
    print(f"{date}: {present}")

# 4. Set operations
print("\n--- Set Operations ---")
dates = list(attendance.keys())
if len(dates) >= 2:
    day1 = attendance[dates[0]]
    day2 = attendance[dates[1]]

    print(f"Students present both days (intersection): {day1 & day2}")
    print(f"Students present at least one day (union): {day1 | day2}")
    print(f"Students absent on day 2 but present on day 1 (difference): {day1 - day2}")

# 5. Dictionary methods
print("\n--- Dictionary Methods ---")
print("Dates recorded:", attendance.keys())
print("Attendance values:", attendance.values())
print("Items:", attendance.items())

# Check if a specific student was present on a specific day
check_date = dates[0]
student_to_check = "Alice"
was_present = student_to_check in attendance.get(check_date, set())
print(f"\nWas {student_to_check} present on {check_date}? -> {was_present}")

# 6. Adding a new student (tuple is immutable)
print("\n--- Tuple Immutability ---")
print("Original students:", students)
# Tuples cannot be changed, but we can create a new tuple
new_students = students + ("Frank",)
print("Updated students (new tuple):", new_students)

# 7. Summary
print("\n--- Attendance Summary ---")
for student in new_students:
    present_days = sum(student in present for present in attendance.values())
    print(f"{student}: Present {present_days} day(s)")