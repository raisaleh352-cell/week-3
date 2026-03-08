# parking meter.py
# date: 2024-06-01
print("Kia ora, this is a parking meter!")
park_time = 4
rate = 4  # $4 per hour for the first 3 hours
cost = 0
print("park_time is", park_time, "hours")
if park_time > 3:
    cost = 12  # $3 per hour for the first 3 hours
    # drop the rate by $2
    rate = 2
    # get the remainder of the parking time
    remaining_time = park_time - 3
    # add to the current cost
    cost += rate * remaining_time
    print("The cost of the parking is $", cost)
else:
    cost = 4 * park_time
    print("The cost of the parking is $", cost)
total_cost = cost
print("The total cost of the parking is $", total_cost)