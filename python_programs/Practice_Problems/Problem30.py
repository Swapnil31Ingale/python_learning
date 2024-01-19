# The current population of a town is 10000. The population of the town is 
# increasing at the rate of 10% per year. You have to write a program to 
# find out the population at the end of each of the last 10 years. 
# For eg current population is 10000 so the output should be like this:
# 10th year - 10000
# 9th year - 9000
# 8th year - 8100 and so on

# class Population:
#     def __init__(self):
#         self.population = 10000
#         self.year = 10
    
#     def getPopulation(self):
#         for year in range(1, self.year + 1):
#             self.population = self.population + (self.population * 0.1)
#             print(f"Population at {year} is {int(self.population)}.")
            
# obj = Population()
# obj.getPopulation()

class Population:
    def __init__(self):
        self.population = 10000
        self.year = 10
    
    # def ordinal(self, number):
    #     if number % 10 == 1 and number % 100 != 11:
    #         suffix = 'st'
    #     elif number % 10 == 2 and number % 100 != 12:
    #         suffix = 'nd'
    #     elif number % 10 == 3 and number % 100 != 13:
    #         suffix = 'rd'
    #     else:
    #         suffix = 'th'
    #     return f"{number}{suffix}"

    def ordinal(self, number):
        if 10 <= number % 100 <= 20:
            suffix = 'th'
        else:
            suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')
        return f"{number}{suffix}"

    def getPopulation(self):
        # Print the population for the 10th year separately
        print(f"{self.ordinal(10)} year - {int(self.population)}")
        for year in range(self.year - 1, 0, -1):
            self.population = self.population - (self.population * 0.1)
            print(f"{self.ordinal(year)} year - {int(self.population)}")  

# Create an instance of the Population class
obj = Population()

# Call the getPopulation method
obj.getPopulation()

            
        
    