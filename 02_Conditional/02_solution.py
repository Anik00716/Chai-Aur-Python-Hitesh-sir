age = 26
day = "Wednesday"


price = 12 if age >= 18 else 8

price = price -2 if day == "Wednesday" else price
# if day == "Wednesday":
#     price = price - 2 # or we can write price -=2

print("Ticket price for you is $", price)