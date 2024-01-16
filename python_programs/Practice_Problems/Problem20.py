# Write a program that will give you the in hand salary after deduction 
# of HRA(10%),DA(5%),PF(3%), and tax(if salary is between 5-10 lakh–10%),
# (11-20lakh–20%),(20< _   – 30%)(0-1lakh print k).

class In_Hand_Salary:
    def __init__(self, salary):
        # self.salary = int(salary)
        self.salary = salary
        print(f"Total salary is Rs.{self.salary}L")
    
    def standardDeductions(self):
        deductions = self.salary * (10/100) + self.salary * (5/100) + self.salary * (3/100)
        return deductions
        
    def tax(self):  
        if self.salary >= 5 and self.salary <= 10:
            tax = self.salary * 10/100
        elif self.salary >= 11 and self.salary <= 20:
            tax = self.salary * 20/100
        elif self.salary > 20:
            tax = self.salary * 30/100
        else:
            tax = 0
        return tax

# # Take salary input from the user
# user_salary = input("Enter the salary: ")

# # Creating an instance of the class with the provided salary
# obj = In_Hand_Salary(salary=user_salary)

obj = In_Hand_Salary(15)

d1 = obj.standardDeductions()
d2 = obj.tax()

all_deductions = d1 + d2

I_H_Salary = obj.salary - all_deductions
print(f"In-hand Salary is Rs.{I_H_Salary}L")
            
        