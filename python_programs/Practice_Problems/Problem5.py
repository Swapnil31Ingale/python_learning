# Write a program that will reverse a four digit number.
# Also it checks whether the reverse is true.

#1234 --> 4321

l = []
user_input = int(input("Enter a four digit number: "))
no = user_input

a = no % 10 #(1234 % 10 = 4)
no = no // 10 #(1234 // 10 = 123)
b = no % 10 #(123 % 10 = 3)
no = no // 10 #(123 // 10 = 12)
c = no % 10 #(12 % 10 = 2)
d = no // 10 #(12 // 10 = 1)

l.append(str(a))
l.append(str(b))
l.append(str(c))
l.append(str(d))

# print(l)
reverse_no = "".join(l)
print(f"The reverse of the {user_input} is {reverse_no}.")