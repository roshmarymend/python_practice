import re

email = input("Enter email address: ")

if re.match(r'^[\w.-]+@[\w.-]+\.\w+$', email):
    print("Valid email")
else:
    print("Invalid email")

phone = input("Enter phone number: ")

if re.match(r'^[6-9]\d{9}$', phone):
    print("Valid phone number")
else:
    print("Invalid phone number")

log = input("Enter log message: ")

ids = re.findall(r'TXN\d+', log)

print("Transaction IDs:", ids)

