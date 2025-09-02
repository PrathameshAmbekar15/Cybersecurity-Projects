import re

password = input("Enter your password: ")

if len(password) < 8:
    print("Too short")
elif not re.search("[a-z]", password):
    print("Add lowercase letters")
elif not re.search("[A-Z]", password):
    print("Add uppercase letters")
elif not re.search("[0-9]", password):
    print("Add digits")
elif not re.search("[!@#$%^&*()]", password):
    print("Add special characters")
else:
    print("Strong password ✅")
