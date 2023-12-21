# Snake Water Gun
# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors"
# where players use hand gestures to represent a snake, water, or a gun. The gun 
# beats the snake, the water beats the gun, and the snake beats the water. 
# Write a python program to create a Snake Water Gun game in Python using if-else 
# statements. Do not create any fancy GUI. Use proper functions to check for win.

import random
import sys


user_choice = int(input("Please Enter your choice  between 1. Snake, 2. Water, 3. Gun: "))
comp_choice = random.choice([1, 2, 3])
dict = {"Snake": 1 , "Water": 2, "Gun": 3}

# print(user_choice, comp_choice)

if user_choice == 1 and comp_choice == 1:
    print("Draw")
elif user_choice == 1 and comp_choice == 2:
    print("User Won")
elif user_choice == 1 and comp_choice == 3:
    print("User Lose")
elif user_choice == 2 and comp_choice == 1:
    print("User Lose")
elif user_choice == 2 and comp_choice == 2:
    print("Draw")
elif user_choice == 2 and comp_choice == 3:
    print("User Won")
elif user_choice == 3 and comp_choice == 1:
    print("User Won")
elif user_choice == 3 and comp_choice == 2:
    print("User Lose")
elif user_choice == 3 and comp_choice == 3:
    print("Draw")
else:
    print("Invalid Choice")
    sys.exit
    
# import random

# def check(comp, user):
#   if comp ==user:
#     return 0
    
#   if(comp == 0 and user ==1):
#     return -1
    
#   if(comp == 1 and user ==2):
#     return -1
    
#   if(comp == 2 and user == 0):
#     return -1

#   return 1
    
  
# comp = random.randint(0, 2)
# user = int(input("0 for Snake, 1 for water and 2 for Gun:\n"))

# score = check(comp, user)

# print("You: ", user)
# print("Computer: ", comp)