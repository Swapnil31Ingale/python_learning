import sys
import random

preference = int(input("Please choose one option betwween 1.Coding 2.Decoding: "))

messgae = input("Please provide the word to Code/Decode: ")
words = messgae.split()
random_chars = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))

if preference == 1:
    code_list = []
    print("You have chosen Coding")
    for word in words:
        if len(word) >= 3:
            first_char = word[0]
            coded_word = random_chars + word[1:] + first_char + random_chars
            code_list.append(coded_word)
        else:
            code_list.append(word[::-1])
    print("Secret Code is: ", ' '.join(code_list))
elif preference == 2:
    decode_list = []
    print("You have chosen Decoding")
    for word in words:
        if len(word) >= 3:
            rem_3 = word[3:-3]
            decoded_word = rem_3[-1] + rem_3[:-1]
            decode_list.append(decoded_word)
        else:
            decode_list.append(word[::-1])
    print("Decoded word is:", ' '.join(decode_list))
else:
    print("Invalid Input")
    sys.exit()