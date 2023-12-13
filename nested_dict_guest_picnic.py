# allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
#             'Bob': {'ham sandwiches': 3, 'apples': 2},
#             'Carol': {'cups': 3, 'apple pies': 1}}
# def totalBrought(item):
#     numBrought = 0
#     for k, v in allGuests.items():
#         numBrought = numBrought + v.get(item, 0)
#     return numBrought
# print('Number of things being brought:')
# print(' - Apples ' + str(totalBrought('apples')))
# print(' - Cups ' + str(totalBrought('cups')))
# print(' - Cakes ' + str(totalBrought('cakes')))
# print(' - Ham Sandwiches ' + str(totalBrought('ham sandwiches')))
# print(' - Apple Pies ' + str(totalBrought('apple pies')))

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
            'Bob': {'ham sandwiches': 3, 'apples': 2},
            'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(dict, item):
    numBrought = 0
    for k, v in dict.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought
print('Number of things being brought:')
print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies ' + str(totalBrought(allGuests, 'apple pies')))