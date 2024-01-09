# Write a program to find the simple interest when the value of principle,
# rate of interest and time period is given.

principle_amount = float(input("Please enter Principle Amount: "))
ROI = float(input("Please enter Rate Of Interest %: "))
Time = float(input("Please enter Time in year: "))

simple_interest = (principle_amount * ROI * Time) / 100

print(f"Simple Interest is {simple_interest}!")

