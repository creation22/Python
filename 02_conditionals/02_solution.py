userage = int(input("enter the age of the person"))
day ="Wednesday"

price = 12  if userage >= 18 else 8

if day == "Wednesday":
    price -= 2 
    # price = price -2 
# print(price)
print("price of the movie ticket is $" ,price)