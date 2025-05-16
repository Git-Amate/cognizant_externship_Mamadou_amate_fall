password = input("let's check your password : ")

# Initialize flags
has_upper = False
has_lower = False
has_digit = False
has_special = False


# Check each character in the password
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char == '@' or char == '&' or char == '$':
        has_special = True

if len(password) < 8:
    print("Your password must be at least 8 characters long.")
if not has_upper:
    print("Your password needs at least one uppercase letter.")
if not has_lower:
    print("Your password needs at least one lowercase letter.")
if not has_digit:
    print("Your password needs at least one digit.")
if not has_special:
    print("Your password needs at least one special character (@, #, $).")
if has_special and has_digit and has_lower and has_upper and len(password)>8:
    print("Your password is strong! 💪")
