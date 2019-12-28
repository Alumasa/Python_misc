#this is a shopping calculator
#these are fruits available and their costs
banana_cost = 10
apple_cost = 25
mango_cost = 10

#the user is informed and asked to choose a fruit to buy
input_fruit = input("""Choose between: Banana, Apple and Mango.
Which fruit would you like to buy?:""")

#the choice is counted
input_count = input("How many " + input_fruit.lower() + "s do you want?:")
count = int(input_count)

#money input is taken
input_money = input("How much money do you have?:")
money = int(input_money)

#total cost is calculated
if input_fruit.lower() == "banana" and input_fruit.isalpha():
    total_cost = banana_cost * count
elif input_fruit.lower() == "apple" and input_fruit.isalpha():
    total_cost = apple_cost * count
elif input_fruit.lower() == "mango" and input_fruit.isalpha():
    total_cost = mango_cost * count
else:
    print("empty")

print("The total price is " + str(total_cost) + " Kenya Shillings")

#conditions for purchase -  compare money and cost
if money > int(total_cost):
     print("You have bought " + str(input_count) + " " + input_fruit.lower() + "s.")
     print("You have " + str(money - int(total_cost)) + " Kenya Shillings left.")

elif money == int(total_cost):
     print("You have bought " + str(input_count) + " " + input_fruit.lower() + "s.")
     print("Your wallet is empty.")

else:
     print("You don\'t have enough money.")
     print("You cannot buy that many " + input_fruit.lower() + "s.")
