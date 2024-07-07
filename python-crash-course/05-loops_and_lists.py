#    _                          
#   | |    ___   ___  _ __  ___ 
#   | |   / _ \ / _ \| '_ \/ __|
#   | |__| (_) | (_) | |_) \__ \
#   |_____\___/ \___/| .__/|___/
#                    |_|        

# Chapter 4
# From page 49 to ??

magicians = ['alice', 'david', 'carolina']

# Ecco come si fanno i for loop:

for magician in magicians:
    print(magician)
# cioe', per ogni elemento generico, che chiameremo 'magician', che sta nella lista 'magicians' esegui print(magician)

numbers = list(range(1,6))
print(numbers)
# Output: [1, 2, 3, 4, 5]

numbers = list(range(0,11,2)) # from 0 to 10(11-1) with step 2, so even numbers only 
print(numbers)

squares = [] # empty list
for value in range(1,11):
    squares.append(value**2)
print(squares)    
print(f"max(squares): {max(squares)}")
print(f"sum(squares): {sum(squares)}")

# List Comprehension: pag 59 - praticamente tutto condensatissimo
cubes = [value**3 for value in range(1,11)]
print(cubes) # output: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

print(cubes[2:5]) # output: [27, 64, 125]
# SE lasci uno dei 2 parametri vuoti va fino all'ultimo/inizia dal primo. esempio: [2:] o [:4] | e ovviamente fnziona coi soliti indici negativi es: [0:-2]

###### pag 63















