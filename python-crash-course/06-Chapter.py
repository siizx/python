#    ____  _      _   _                        _           
#   |  _ \(_) ___| |_(_) ___  _ __   __ _ _ __(_) ___  ___ 
#   | | | | |/ __| __| |/ _ \| '_ \ / _` | '__| |/ _ \/ __|
#   | |_| | | (__| |_| | (_) | | | | (_| | |  | |  __/\__ \
#   |____/|_|\___|\__|_|\___/|_| |_|\__,_|_|  |_|\___||___/
                                                          

# Chapter 6
# Page 91 to

# Simple dictionary:
print("# Simple Dictionary:")

#alien_0 = {} # crea un dizionario vuoto.
alien_0 = {'color': 'green', 'points': 5}
print(f"alien_0 -> 'color': {alien_0['color']}, 'points': {alien_0['points']}")

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_0['color'] = 'yellow'
print(alien_0)

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

alien_0['speed'] = 'medium'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien!
    x_increment = 3

# Update the alien's position:
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"The new alien_0's x_position is {alien_0['x_position']}")

# Deletion of a key-value pair
alien_0['tentacle_penis_lenght_in_meters'] = 4
print(alien_0)
del alien_0['tentacle_penis_lenght_in_meters']
print(alien_0)

# Space line
print("\n")


favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }

# get() to access values:
print("print(alien_0['hight']) NON ESISTEi, ma con get(), possiamo assegnare ai valori inesistenti, un valore di default.\nPer esempio:")
height_value = alien_0.get('height', 'No height value assigned.')
print(height_value)


# Space line
print("\n")

user_0 = {
        'username': 'efermi',
        'name': 'enrico',
        'last': 'fermi',
        }

# Space line
print("\n")

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


for n,l in favorite_languages.items():
    print(f"\n{n.title()}'s favorite language is {l.title()}")

# Space line
print("\n")

print("Looping though the keys is actually the default behavior when looping through a dictionary, so:\n'for name in favorite_languages:'\nand\n'for name in favorite_languages.keys():'\nhave the same output!\n")

for k in favorite_languages.keys():
    print(f"{k.title()}")
