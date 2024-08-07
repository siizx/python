# Chapter 8
# Page 136
# Funciton calls


# questa funzione ha 'dog' come parametro di default per pet_type.
# se l'animale non dovesse essere un cane, basta passare il tipo come argomento
# (esempio sotto)
def describe_pet(pet_name,pet_type='dog'):
    print(f"\nI have a {pet_type}.")
    print(f"My {pet_type}'s name is {pet_name.title()}.")

describe_pet('giraffe', 'gigi')
describe_pet('camilla')

# equivalent function calls:
print("\nEquivalent funciton calls:")
describe_pet('buffon','cat')
describe_pet(pet_type='cat', pet_name='buffon')

# Invalid function because python wants the undefined default value FIRST.
# def describe_pet2(pet_type='dog',pet_name):
    # print(f"\nI have a {pet_type}.")
    # print(f"My {pet_type.title()}'s name is {pet_name}.")
