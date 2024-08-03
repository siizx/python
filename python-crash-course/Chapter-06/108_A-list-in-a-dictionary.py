# Chapter 6
# Page 108
# A list in a dictionary:

#store information about a pizza being ordered:

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
print(pizza['toppings'])


print("\n")#######

favorite_languages = {
    'tom': ['c','java'],
    'jay': ['c','html'],
    'samantha': ['javascript', 'python'],
    'sarah': ['ruby', 'go']
}

for name,languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")


