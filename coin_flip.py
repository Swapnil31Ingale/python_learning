import random

def generate_coin_flips():
    return ['H' if random.randint(0, 1) == 0 else 'T' for _ in range(100)]

def has_streak(flips, streak_length):
    for i in range(len(flips) - streak_length + 1):
        if all(flips[i + j] == flips[i] for j in range(1, streak_length)):
            return True
    return False

numberOfStreaks = 0
streak_length = 6
total_experiments = 10000

for experimentNumber in range(total_experiments):
    coin_flips = generate_coin_flips()
    if has_streak(coin_flips, streak_length):
        numberOfStreaks += 1

percentage_of_streaks = (numberOfStreaks / total_experiments) * 100
print('Chance of streak: %s%%' % percentage_of_streaks)


# import random

# def generate_coin_flips():
#     return ''.join(random.choice(['H', 'T']) for _ in range(100))

# def has_streak(flips, streak_length):
#     return 'HHHHHH' in flips or 'TTTTTT' in flips

# numberOfStreaks = 0
# streak_length = 6
# total_experiments = 10000

# for experimentNumber in range(total_experiments):
#     coin_flips = generate_coin_flips()
#     if has_streak(coin_flips, streak_length):
#         numberOfStreaks += 1

# percentage_of_streaks = (numberOfStreaks / total_experiments) * 100
# print(f'Chance of streak: {percentage_of_streaks}%')

