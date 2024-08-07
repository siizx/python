# Chapter 7
# Page 126
# Filling a dictionary with user input

responses = {}

# set a flag to indicate that polling is active:
polling_active = True

while polling_active:
    name = input("\nWhat's your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # store the response in the dictionary:
    responses[name] = response

    # find out if someone else is going to take the poll:
    repeat = input("Would you like to let another person take the poll? (yes/no)\n")
    if repeat == "no":
        polling_active = False
    
    # Polling is complete. Show the result:
print("\n--- POLL RESULT ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")