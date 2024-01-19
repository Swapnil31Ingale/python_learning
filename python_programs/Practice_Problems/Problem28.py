# Write a program to print whether a given number is prime 
# number or not

def is_prime(number):
    if number <= 1:
        print(f"{number} is not a prime number")
    else:
        for i in range(2, number):
            if number % i == 0:
                print(f"{number} is not a prime number")
                break
        else:
            print(f"{number} is a prime number")

number = int(input("Please enter a number: "))
is_prime(number)
