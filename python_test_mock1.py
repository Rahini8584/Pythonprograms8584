try:
    a=float(input())
    b=float(input())
    print(a/b)
except ValueError:
    print("Error :please enter the numeric value only")
except ZeroDivisionError:
    print("Error : division by zero is not allowed  ")
finally:
    print("Attempt Completed ") 