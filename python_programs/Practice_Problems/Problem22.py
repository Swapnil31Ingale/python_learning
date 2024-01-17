# Write a program that will tell the number of dogs and 
# chicken are there when the user will provide the value of 
# total heads and legs.

H = int(input("Enter the number of heads: "))
L = int(input("Enter the number of legs: "))

class Animals:
    def __init__(self, H, L):
        self.H = H
        self.L = L

    def count(self):
        # Calculate the number of dogs and chickens
        # Assuming a dog has 4 legs and a chicken has 2 legs
        # The total legs equation is: 4 * num_dogs + 2 * num_chickens = total_legs

        # Solving the equations
        num_chickens = (self.L - 4 * self.H) / 2
        num_dogs = self.H - num_chickens

        # Check if the calculated values are non-negative integers
        if num_chickens >= 0 and num_dogs >= 0 and num_chickens.is_integer() and num_dogs.is_integer():
            return int(num_dogs), int(num_chickens)
        else:
            return "Invalid input. Unable to determine the number of dogs and chickens."

# Create an instance of the Animals class
animal_instance = Animals(H, L)

# Call the count method to get the result
result = animal_instance.count()

# Print the result
print(result)

