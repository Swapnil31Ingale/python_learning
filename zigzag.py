# import time, sys
# indent = 0 # How many spaces to indent.
# indentIncreasing = True # Whether the indentation is increasing or not.
# try:
#     while True: # The main program loop.
#         print(' ' * indent, end='')
#         print('********')
#         time.sleep(0.1) # Pause for 1/10 of a second.
#         if indentIncreasing:
#             # Increase the number of spaces:
#             indent = indent + 1
#             if indent == 10:
#                 # Change direction:
#                 indentIncreasing = False
#         else:
#             # Decrease the number of spaces:
#             indent = indent - 1
#             if indent == 0:
#                 # Change direction:
#                 indentIncreasing = True
# except KeyboardInterrupt:
#     sys.exit()

import time
import sys
counter = 0
counterIncrease =  True

try:
    while True:
        print(" " * counter, end='')
        print("**********")
        time.sleep(0.2)
        if counterIncrease == True:
            counter = counter + 1
            if counter == 5:
                counterIncrease =  False
        else:
            counter = counter - 1
            if counter == 0:
                counterIncrease =  True
except KeyboardInterrupt:
    sys.exit()
            
                

