# Chapter 7
# Page 124
# Moving Items from one dictionary to another:

unconfirmed_users = ['andrea', 'desi', 'batman', 'robin',]
confirmed_users = []

# STAMPO LE LISTE
print("\nUnverified Users:")
if not unconfirmed_users:
    print("\t~ NONE")
else:
    for u in unconfirmed_users:
        print(f"\t- {u}")

print("\nVerified Users:")
if not confirmed_users:
    print("\t~ NONE")
else:
    for u in confirmed_users:
        print(f"\t- {u}") 


print("\n")#############
# confermo gli users:
for u in range(len(unconfirmed_users)-1,-1, -1):
    print(f"Verifying user {u} '{unconfirmed_users[u]}'")
    confirmed_users.append(unconfirmed_users.pop())

# STAMPO LE LISTE:
print("\nUnverified Users:")
if not unconfirmed_users:
    print("\t~ NONE")
else:
    for u in unconfirmed_users:
        print(f"\t- {u}")

print("\nVerified Users:")
if not confirmed_users:
    print("\t~ NONE")
else:
    for u in confirmed_users:
        print(f"\t- {u}") 
    
