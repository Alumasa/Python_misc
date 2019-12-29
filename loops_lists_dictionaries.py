#this is a shopping list calculator using lists, loops and dictionaries
#this is a list
shopping_list = ["banana", "orange", "apple", "pear"]

#this is a dictionary
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

#another dictionary
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


# a function to compute total, and reduce stock
def compute_bill(food):
    total = 0.0
    for item in food:
        if (stock[item]) > 0:
            total += prices[item]
            stock[item] -= 1
    return total


print(compute_bill(shopping_list))