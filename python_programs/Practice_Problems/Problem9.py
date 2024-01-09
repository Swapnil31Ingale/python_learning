# Write a program that take a user input of three angles and will find out 
# whether it can form a triangle or not.

angle1 = int(input("First angle: "))
angle2 = int(input("Second angle: "))
angle3 = int(input("Third angle: "))

if (angle1 + angle2 + angle3 == 180) and angle1 != 0 and angle2 != 0 and angle3 != 0:
    print("Triangle can be formed")
else:
    print("Triangle cannot formed")