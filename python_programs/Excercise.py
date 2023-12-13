import random

spam = 0
spam = random.randint(1, 3)
#print(spam)

if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")

for i in range(0, 10):
    print(i)
    
i = 0
while i < 11:
    print(i)
    i = i + 1