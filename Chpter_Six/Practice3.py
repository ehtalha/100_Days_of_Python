# Grade Calculator
score = int(input("Enter student number : "))
print(f"Entered number is : {score}")
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Enter student number : 99
# Entered number is : 99
# Grade: A

# Leap Year Finder
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# output
# 2024 is a leap year.