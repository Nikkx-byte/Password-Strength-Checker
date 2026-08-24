password = input("Enter a password to check: ")

length_ok = len(password) >= 8
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_number = any(char.isdigit() for char in password)
has_special = any(char in "!@#$%^&*()_+-=" for char in password)

score = sum([length_ok, has_upper, has_lower, has_number, has_special])

print("")
print("Length 8+:", length_ok)
print("Has uppercase:", has_upper)
print("Has lowercase:", has_lower)
print("Has number:", has_number)
print("Has special character:", has_special)

print("")
if score <= 2:
    print("Password Strength: WEAK")
elif score <= 4:
    print("Password Strength: MEDIUM")
else:
    print("Password Strength: STRONG")