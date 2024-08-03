favorite_languages = {
    'klara' : 'python',
    'jenny' : 'c',
    'marco' : 'java',
    'annah' : 'c',
    'tommy' : 'go'
}
names_list = {
    'klara',
    'jenny',
    'penny',
    'russel',
    'marco',
    'annah',
    'cindy',
    'tommy'
}

print("\n1) Loop in default order:")

for k in names_list:
    if k in favorite_languages:
        print(f"Thanks {k.title()} for taking the poll!")
    else:
        print(f"Please {k.title()} take the poll.")

print("\n2) Loop in order:")

for k in sorted(names_list):
    if k in favorite_languages:
        print(f"Thanks {k.title()} for taking the poll!")
    else:
        print(f"Please {k.title()} take the poll.")