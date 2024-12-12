import re
def validate_username(username):
    if len(username) < 5:
        return False
    if not re.match(r'^[a-zA-Z0-9]+$', username):
        return False
    return True
invalid_username =["Invalid username"]
def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]',password) or not re.search(r'[a-z]', password) or not re.search(r'\d', password):
        return False
    return True
invalid_password = ["Invalid password"]
while True:
    username = input("Enter your username: ")
    if validate_username(username):
        break
else:
    print(invalid_username)

while True:
    password = input("Enter your password:" )
    if validate_password(password):
        break
else:
    print(invalid_password)
print("Registration Successful!")    