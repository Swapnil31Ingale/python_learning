# Write a program that will tell whether the number entered by the user is odd or even.

user_no = int(input("Please enter a number: "))

def check(number):
    if user_no % 2 == 0:
        print(f"{user_no} is Even")
    else:
        print(f"{user_no} is Odd")
        
check(user_no)
    