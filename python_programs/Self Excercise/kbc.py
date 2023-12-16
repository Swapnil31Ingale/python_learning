# #KBC Game#

# Question, 4 options, correct ans, take user ans, 
# check for correct ans, add money

questions_answers = [
["A means?", "Apple", "Ball", "Cat", "Dog", 1],
["B means?", "Apple", "Ball", "Cat", "Dog", 2],
["C means?", "Apple", "Ball", "Cat", "Dog", 3],
["D means?", "Apple", "Ball", "Cat", "Dog", 4],
["E means?", "Egg", "Ball", "Cat", "Dog", 1],
["F means?", "Apple", "Full", "Cat", "Dog", 2],
["G means?", "Apple", "Ball", "Goat", "Dog", 3],
["H means?", "Apple", "Ball", "Cat", "Horse", 4],
["I means?", "Ice", "Ball", "Cat", "Horse", 1],
["J means?", "Apple", "Jet", "Cat", "Horse", 2]
]

#print(len(questions_answers))
money = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000]
i = 0
fixed_money = 0

for i in range(0, len(questions_answers)):
    question = questions_answers[i]
    print ("#"*50)
    print(f"Your question for Rs. {money[i]} is {question[0]}")
    print(f"a. {question[1]}      b. {question[2]}")
    print(f"c. {question[3]}      d. {question[4]}\n")
    user_ans = int(input("Please select your answer from options (1-4) or 0 for quit:\n"))
    if user_ans == 0:
        fixed_money = money[i-1]
        print("You have chosen to quit the Game, Best wishes for your future!!")
        break
    if user_ans not in (1, 2, 3, 4):
        print("Invalid answer no, please select the correct answer from (1-4)")
        break
    if user_ans == question[5]:
        print(f"Correct answer, You have won: {money[i]}\n")
        if i == 4:
            fixed_money = 10000
        elif i == 9:
            fixed_money = 320000
        elif i == 14:
            fixed_money = 10000000
    elif user_ans != question[5]:
        print(f"\nWrong answer, the correct answer is {question[5]}.")
        print(f"You will take Rs. {fixed_money} to home.")
        break
        
    
    