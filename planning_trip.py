#this calculates cost of a holiday in kenya using functions
#this function calculates the cost of hotel rooms with number of nights

vanessa = {"name": "vanessa",
           "telephone": "07123456",
           "home": "Kakamega"
           }

alumasa = {"name": "alumasa",
           "telephone": "07986543",
           "home": "Nairobi"
           }
chantal = {"name": "chantal",
           "telephone": "07654320",
           "home": "Mombasa"}

username = input("Please enter your username: ")

#customers1 = ["vanessa", "alumasa", "chantal"]
def customer_details(customers):
        if vanessa["name"] == username:
            print(vanessa)
        elif alumasa["name"] == username:
            print(alumasa)
        elif chantal["name"] == username:
            print(chantal)
        else:
            print("Username not found in database.")

customers = [vanessa, alumasa, chantal]
customer_details(customers)

confirm = input("Please confirm your details before planning your trip. y/n: ")




def hotel_cost():
    hotel_nights = input("How many nights will you spend?: ")
    nights = int(hotel_nights)
    return 2000 * nights

#this function calculates transport costs
def plane_ride_cost():
    city = input("Where would you like to go?: ")
    if city == "Nairobi":
        return 5500
    elif city == "Mombasa":
        return 10000
    elif city == "Eldoret":
        return 4500
    elif city == "Kisumu":
        return 5000

#this function calculates local transport car hire
def rental_car_cost():
    car_days = input("How many days will you hire a car?: ")
    days = int(car_days)
    total = 5000 * days
    if days >= 7:
        total -= 1000
    elif days >= 3:
        total -= 400
    return total

#this function calls other functions and addds them to find the total cost of the trip.
def trip_cost():
    return rental_car_cost() + hotel_cost() + plane_ride_cost() + spending_money



if confirm == "y":
    spending_money = int(input("How much is your extra money?: "))
    #hotel_cost()
    #plane_ride_cost()
    #rental_car_cost()
    #trip_cost()
    print(trip_cost())
else:
    print("Please change your details before planning.")



#output of the trip cost function
