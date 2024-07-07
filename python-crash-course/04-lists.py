#  _     _     _       
# | |   (_)___| |_ ___ 
# | |   | / __| __/ __|
# | |___| \__ \ |_\__ \
# |_____|_|___/\__|___/

# Chapter 3. 
# From Page ? to 48.

# Look for "!!" for not yet clarified things.

names = ['andrea', 'desire', 'roberto', 'ornella']

print(names)# output: ['andrea', 'desire', 'roberto', 'ornella']

print(f"\t{names[0]}") # output: andrea

print(f"\t{names[-1]}") # output: ornella | cioe' l'ultimo elemento della lista.
print(f"\t{names[-2]}") # output: roberto | penultimo elemento della lista.
# e cosi'  via...

# eccone uno dei tanti utilizzi:
gf = f"\tLa mia ragazza si chiama {names[1].title()}.\n"
print(gf)

# Adding elements:
names.append('chewbecca') # Aggiunge l'elemento in ultima posizione.
print(names)
names.insert(-1, 'camilla') # Aggiunge l'elemento nella posizione indicata nell'argomento.

names.append('vespe')
print(names)
print("\nOh nooo, e ora come le rimuovo le vespe dalla mia lista?")

del names[-1]
# anche names.pop() | .pop(n)
names.append('calabroni')
print(f"\t{names}")
names.remove('calabroni')
print(f"\t{names}")

print("\nOra li ordino con names.sort():", end=" ")
names.sort()
print(names, end="\n")

print("\nOra li ordino con names.sort(reverse=True):", end=" ")
names.sort(reverse=True)
print(names, end="\n\n")
print("Sometimes you just want to print the list sorted out, but also want to keep the original order of the elements in the list.\nIn that case, you can use sorted(names).")
print(sorted(names)) 
# !! print(sorted(names.title())) non funziona... e non so perche'..
print(f"List lenght or size: len(names): {len(names)}")












