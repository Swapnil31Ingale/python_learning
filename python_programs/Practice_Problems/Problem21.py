# Write a menu driven program - 1.cm to ft  2.kl to miles  3.usd to inr  
# 4.exit

import sys

try:
    user_input = int(input('''Please enter your choice:
1. cm to ft
2. kl to miles
3. usd to inr
4. exit\n'''))

    if user_input == 1:
        cm_input = int(input("Please enter the value in cm: "))
        In_feet = cm_input * 0.0328084
        print(f"Converted value is {In_feet} feet!!")
    elif user_input == 2:
        kl_input = int(input("Please enter the value in kl: "))
        In_mi = kl_input * 0.621371
        print(f"Converted value is {In_mi} miles!!")
    elif user_input == 3:
        usd_input = int(input("Please enter the value in usd: "))
        In_inr = usd_input * 83.10
        print(f"Converted value is {In_inr} INR!!")
    elif user_input == 4:
        sys.exit()
    else:
        print("Invalid input")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    
    
# import sys

# def cm_to_ft(cm_input):
#     return cm_input * 0.0328084

# def kl_to_miles(kl_input):
#     return kl_input * 0.621371

# def usd_to_inr(usd_input):
#     return usd_input * 83.10

# while True:
#     print('''Please enter your choice:
#     1. cm to ft
#     2. kl to miles
#     3. usd to inr
#     4. exit''')

#     try:
#         user_input = int(input("Enter your choice (1-4): "))

#         if user_input == 1:
#             cm_input = float(input("Please enter the value in cm: "))
#             result = cm_to_ft(cm_input)
#             print(f"Converted value is {result} feet!!")
#         elif user_input == 2:
#             kl_input = float(input("Please enter the value in kl: "))
#             result = kl_to_miles(kl_input)
#             print(f"Converted value is {result} miles!!")
#         elif user_input == 3:
#             usd_input = float(input("Please enter the value in usd: "))
#             result = usd_to_inr(usd_input)
#             print(f"Converted value is {result} INR!!")
#         elif user_input == 4:
#             print("Exiting program.")
#             sys.exit()
#         else:
#             print("Invalid input. Please enter a number between 1 and 4.")
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")



    
