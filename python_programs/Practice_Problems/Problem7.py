# Write a program that will tell whether the given year is a leap year or not.

year = int(input("Please enter a year: "))

print("Leap Year") if year % 4 == 0 else print("Not a leap year")