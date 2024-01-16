"""
Given the dictionary below, which consists of vehicles and their weights in kilograms:
vehicle_weights = { "Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

Construct a single list comprehension statement to create a list containing the uppercase names of vehicles with weights below 5000 kilograms. 
The solution should be expressed as a single statement within a list, like the example below:
result_list = [use comprehension to achieve the result in a single statement]

Your comprehension should filter vehicles with weights below 5000 kilograms and convert the key names to uppercase in the resulting list.
"""

from dataset import vehicles


# Method that returns the keys of vehicles whose weight is above 5000
def vehicles_below_5000(vehicle_weights):
    return [key.upper() for key, value in vehicle_weights.items() if (value < 5000)]
    

print(vehicles)

