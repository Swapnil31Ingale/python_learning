           
def collatz(number):
        even_check = number % 2
        if even_check == 0:
            print("The entered number is Even")
            even_var = number // 2
            print(even_var)
        elif even_check == 1:
            print("The entered number is Odd")
            odd_var = 3 * number + 1
            print(odd_var)
    
print("Please Enter the number: ")
try:
    number = int(input()) 
    collatz(number)
except ValueError:
        print("Please enter the intger value only!!") 

