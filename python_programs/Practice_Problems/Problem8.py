# Write a program to find the euclidean distance between two coordinates.

x1 = float(input("Please enter the x1 of x coordinate: "))
x2 = float(input("Please enter the x2 of x coordinate: "))
y1 = float(input("Please enter the y1 of y coordinate: "))
y2 = float(input("Please enter the y2 of y coordinate: "))

d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(f"The euclidean distance between two coordinates is {d}")
