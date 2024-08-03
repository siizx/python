# Chapter 6
# page 110
# many_users.py
# A dictionary in a dictionary.

users = {
    'aeinstein': {'first': 'albert', 'last': 'einstein',
                  'location': 'princeton'},
    'mcurie':{'first': 'marie',
              'last': 'curie',
              'location': 'paris'},
}


for username, userinfo in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{userinfo['first']} {userinfo['last']}"
    location = userinfo['location']
    print(f"\t{full_name.title()}")
    print(f"\t{location.title()}")