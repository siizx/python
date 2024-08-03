# chapter 6, page 104
# Looping through all the values
favorite_languages = {
    'klara' : 'python',
    'jenny' : 'c',
    'marco' : 'java',
    'annah' : 'c',
    'tommy' : 'go'
}

print("\n3) The following languages have been mentioned:")
for v in favorite_languages.values():
    print("-",v)
print("\n~~# Come vedi, 'c' viene ripetuto.\n    Per evitare che accada, possiamo usare set():")
print("\n4) The following languages have been mentioned:")
for v in set(favorite_languages.values()):
    print("-",v.title())

print("\nL'ordine potrebbe essere cambiato, perche' nei set l'ordine non conta niente.")
    