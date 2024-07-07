name = "andrea"
surname = "peres"
fullName = f"{name.title()} {surname.title()}"
greeting = f"Hello, {fullName}!"
print(greeting)
print("\nIn older versions of python, you had to use the format function this way:")
print("fullName = \"{} {}\".format(firstName.title(), surname.title())\nEccolo in azione:", end=" ")
fullName2 = "{} {}".format(name.title(), surname.title())
print(fullName2)
      







