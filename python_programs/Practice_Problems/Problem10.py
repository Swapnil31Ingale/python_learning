# Write a program that will take user input of cost price and selling price 
# and determines whether its a loss or a profit

cost_price = int(input("Cost Price: "))
sell_price = int(input("Sell Price: "))

if cost_price < sell_price:
    print("It's a profit")
else:
    print("It's a loss")