####### Pagina 101 - Chapter 6
# Looping through all the keys in a dictionary:
user_0 = {
        'username': 'efermi99',
        'name': 'enrico',
        'last': 'fermi',
        }


### PRINT USER ITEMS ### 
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }

for n,l in favorite_languages.items():
    print(f"\n{n.title()}'s favorite language is {l.title()}")

print("\n") #-------------------------------

print("### Looping though the keys is actually the default behavior when looping through a dictionary, so:\n'for name in favorite_languages:'\nand\n'for name in favorite_languages.keys():'\nhave the same output!\n")

for k in favorite_languages.keys():
    print(f"{k.title()}")
# e' uguale a:
#for k in favorite_languages:
#    print(f"{k.title()}")