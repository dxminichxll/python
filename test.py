password1 = input("Please enter a new password, between 8 and 15 characters: ")
match = False
password2 = ""
while password1 != password2:
    while len(password1) < 8 or len(password1) > 15:
        password1 = input("Password must be between 8 and 15 characters - please re-enter: ")
    password2 = input("Please verify password: ")
    if password1 == password2:
        match = True
        print("Password set")
    else:
    	match = False
