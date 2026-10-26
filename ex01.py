password = str(input("Give me your password :"))

upper = False
lower = False
digit = False
special = False

for character in password:
    if character.upper():
        upper = True
    if character.lower():
        lower = True
    if character in "!@#$%^&":
        special = True

if len(password) >= 8 and upper and lower and digit and special:
    print("Strong Password")
else:
    print("Weak Password")