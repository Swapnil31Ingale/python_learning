# Write a program that will tell the number of dogs and 
# chicken are there when the user will provide the value of 
# total heads and legs.

class Animals:
    def __init__(self, H, L):
        self.H = H
        self.L = L

    def count(self):
        # Calculate the number of dogs and chickens
        # Assuming a dog has 4 legs and a chicken has 2 legs
        # The total heads equation is: total_heads = num_dogs + num_chickens 
        # num_dogs = total_heads - num_chickens
        
        # The total legs equation is: total_legs = 4 * num_dogs + 2 * num_chickens 
        # So, total_legs =  4 * (total_heads - num_chickens) + 2 * num_chickens
        #     total_legs = 4 * total_heads - 4 * num_chickens + 2 * num_chickens
        #     total_legs = 4 * total_heads - 2 * num_chickens
        #     num_chickens = ( 4 * total_heads - total_legs) / 2

        # Solving the equations
        
        num_chickens = (4 * self.H - self.L) / 2
        num_dogs = self.H - num_chickens
        
        # Check if the calculated values are non-negative integers
        if 0 <= num_chickens <= self.H and 0 <= num_dogs <= self.H and num_chickens.is_integer() and num_dogs.is_integer():
            print("No of dogs in the room:", int(num_dogs), "No of chickens in the room:", int(num_chickens))
        else:
            return "Invalid input. Unable to determine the number of dogs and chickens."

# Create an instance of the Animals class
H = int(input("Enter the number of heads: "))
L = int(input("Enter the number of legs: "))
animal_instance = Animals(H, L)

# Call the count method to get the result
result = animal_instance.count()

# Print the result
print(result)



