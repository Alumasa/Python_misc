#this calculates cost of a holiday in kenya using functions
#this functions calculates the cost of hotel rooms with number of nights
def hotel_cost(nights):
    return 2000 * nights

#this function calculates transport costs
def plane_ride_cost(city):
    if city == "Nairobi":
        return 5500
    elif city == "Mombasa":
        return 10000
    elif city == "Eldoret":
        return 4500
    elif city == "Kisumu":
        return 5000

#this function calculates local transport car hire
def rental_car_cost(days):
    total = 5000 * days
    if days >= 7:
        total -= 1000
    elif days >= 3:
        total -= 400
    return total

#this function calls other functions and addds them to find the total cost of the trip.
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money

#output of thr trip cost function
print(trip_cost("Mombasa", 5, 5000))