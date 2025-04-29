# Furniture.py - This program calculates profits and sales prices for a furniture company.

itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00

profit=((retailPrice)-wholesalePrice)
salePrice=(.75*retailPrice)
saleProfit=((salePrice)-wholesalePrice)

print(f"Item Name: " + itemName)
print(f"Retail Price: $" + str(retailPrice))
print(f"Wholesale Price: $" + str(wholesalePrice))
print(f"Profit: $" + str(profit))
print(f"Sale Price: $" + str(salePrice))
print(f"Sale Profit: $" + str(saleProfit))
