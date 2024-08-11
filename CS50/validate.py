from re import search

email = input("whats your email? ").strip()

if search(r"^.+@.+\.com$", email):
    print("Valid")  
else:
    print("Invalid")