import random

for i in range(10):
    print(random.randint(1, 100))

import sys
while True:
    print("Type exit to exit")
    response = input()
    if response == 'exit':
        sys.exit()
    print("You typed " + response + ".")
