"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables
charge = 0.00
numChars=0
woodType= ""
color= ""

# Get input from the user
numChars = int(input("Enter the number of characters on the sign: "))
woodType = input("Enter the type of wood (pine or oak): ")
color = input("Enter the color of the characters (black, white, or gold): ")

# Base charge
charge = 35.00

# Add $4 for each character after the first five
if numChars > 5:
    charge += (numChars - 5) * 4.00

# Add $20 if the wood type is oak
if woodType.lower() == "oak":
    charge += 20.00

# Add $15 if the color is gold
if color.lower() == "gold":
    charge += 15.00

# Output the charge
print("The charge for this sign is $" + str(charge))
