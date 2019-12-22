banana_cost = 5
money = 20
input_count = input("How many bananas do you want?:")
count = int(input_count)
total_cost = banana_cost * count

print("You have bought " + str(input_count) + " bananas.")
print("The total price is " + str(total_cost) + " Kenya Shillings")

if money > int(total_cost):
     print("You have bought " + str(input_count) + " bananas.")
     print("You have " + str(money - int(total_cost)) + " Kenya Shillings left.")

elif money == int(total_cost):
     print("You have bought " + str(input_count) + " bananas.")
     print("Your wallet is empty.")

else:
     print("You dont have enough money.")
     print("You cannot buy that many bananas.")
