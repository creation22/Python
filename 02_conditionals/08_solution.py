password = "fdsdsf"
password_length = len(password)

if password_length > 10 :
    print("strong password")
elif password_length > 5:
    print("moderate password")
else :
    print("easy password")