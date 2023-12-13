tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    maxList = []
    for x in tableData:
        maxValue = 0
        i = 0
        for y in x:
            if len(x[i]) > maxValue:
                maxValue = len(x[i])
           # print(len(x[i]))
          #  print(x[i])
            i += 1
        maxList.append(maxValue)
    print(maxList)
    
    for i in range(len(tableData[0])):
        for x in range(len(tableData)):
            print(tableData[x][i].rjust(maxList[x]),end = ' ')
            if x == len(tableData)-1:
                print('\r')

printTable(tableData)

# [8, 5, 5]
#   apples Alice  dogs 
#  oranges   Bob  cats 
# cherries Carol moose 
#   banana David goose