import numpy as np

# array = np.array([1,2,3,4])
# print(array)
# array = array*2
# print(array)


#Create an array of 6 clothing prices — use real prices, like things you'd actually buy. Then find and print the min, max, mean and total.

clothes = np.array(["shirt","tshirt","skirt","shorts","pants","socks"])
prices = np.array([400,350,400,300,900,100])

total_price= np.sum(prices)
print("the most expensive thing on the list is of ruppess ", prices.max())                   #or we can use np.max(prices)
print("the most cheapest thing on the list is of ruppess ", prices.min())
print("total cost of wardrobe is " , total_price)
print("avg rate of clothes is " , np.average(prices))

