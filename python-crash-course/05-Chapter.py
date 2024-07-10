#     ____                _ _ _   _                   _     
#    / ___|___  _ __   __| (_) |_(_) ___  _ __   __ _| |___ 
#   | |   / _ \| '_ \ / _` | | __| |/ _ \| '_ \ / _` | / __|
#   | |__| (_) | | | | (_| | | |_| | (_) | | | | (_| | \__ \
#    \____\___/|_| |_|\__,_|_|\__|_|\___/|_| |_|\__,_|_|___/

# Chapter 5
# Page 72





print("\n# Comparazioni tra numeri:")
andrea = 70
desi = 31
roberto = 69

eta = [andrea,desi,roberto]
print(f"\n Checking multiple conditions ((roberto > andrea) and (roberto > desi)) -> {(roberto > andrea) and (roberto > desi)}")
print(f"\n Checking whether a value is/isnt in a list: 'andrea in eta' -> {andrea in eta}")
print("\n Or, with 'bannedUsers = ['andrew','anna','maria']', check if 'sarah' can write a post:")

bannedUsers = ['andrew','anna','maria']
user = 'sarah'
if user not in bannedUsers:
    print(f" {user} has the permission to write a post.")

print("\n# Example of if statement:")
cars = ['toyota','fiat','bmw','lotus','lamborghini']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print("\n# The if-elif-else chain:")

age = 17

#if age < 4:
#    print(" Admission for anyone under age of 4 is free.")
#elif ((age >= 4) and (age < 18)): 
#    print(" Admission for anyone between the ages of 4 and 18 is $25.")
#elif (age >= 18): 
#    print(" Admission for anyone age of 18 or older is $40.")

# or even better:

if age < 4:
    price = 0
elif ((age >= 4) and (age < 18)): 
    price = 25
elif (age >= 18): 
    price = 40
print(f" Your admission cost is ${price}.")


print("\n# PIZZA:")
requestedToppings = []

if requestedToppings:
    for requestedTopping in requestedToppings:
        print(f"Adding {requestedTopping}...")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
