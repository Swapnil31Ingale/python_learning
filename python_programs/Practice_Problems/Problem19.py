# Write a program that will take user input of (4 digits number) and 
# check whether the number is narcissist number or not.

# 1634 = 4**4 + 3**4 + 6**4 + 1**4 

a = input("Enter the number: ")

def getResult(a):
    sum = 0
    length = len(a)
 
    # Traversing through the string
    for i in a:
 
        # Converting character to int
        sum = sum + int(i) ** length
 
    # Converting string to integer
    number = int(a)
 
    # Comparing number and sum
    if (number == sum):
        return "true: Narcissistic no", number
    else:
        return "false: Non-Narcissistic no", number
  
print(getResult(a))
