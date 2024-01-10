# Write a program to find the volume of the cylinder. 
# Also find the cost when ,when the cost of 1 litre milk is 40Rs.

radius = float(input("Enter the radius: "))
height = float(input("Enter the height: "))

volume = 3.14*(radius**2)*height
cost = (volume/1000) * 40

print(f"Cost is {cost}")

