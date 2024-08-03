# chapter 6
# page 106
# A list of Dictionaries:

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

print("\n1) Creati 3 alieni e messi in una lista.\nEcco la lista:")
for a in aliens:
    print(a)

print("\n2) Ora creo una lista vuota e la popolo con 30 alieni utilizzando un for loop:")

alieni = []

for alien_number in range(30):
    new_alien = {
        'color': 'green',
        'points': 5,
        'speed': 'slow'
    }
    alieni.append(new_alien)

#print(alieni)

counter = 1
for a in alieni:
    print(f"    alien_{counter}: {a}")
    counter+=1

print("\nTotal number of aliens:", len(alieni))

print("\n3) Modifichiamo alcuni alieni, facendoli dif=ventare nemici piu abili:")

for alien in alieni[:3]:
    alien['color'] = 'yellow'
    alien['points'] = 10
    alien['speed'] = 'medium'

print("\n~ now printing the first 5 aliens:")
for alien in alieni[:5]:
    print(alien)
print("...")

print("\n4) Potremmo avere gia alieni gialli, quindi modifichiamo il for loop:")

for alien in alieni[:4]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

print("\n~ now printing the first 5 aliens:")
for alien in alieni[:5]:
    print(alien)
print("...")