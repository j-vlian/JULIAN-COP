AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
while True:
    print("******************************************\n    Autocountry Vehicle Finder v0.1    \n******************************************\nPlease Enter the following number below from the following menu:\n\n1.PRINT all authorized vehicles\n2. Search\n3. Exit\n")

    menuSelect=int(input())
    if menuSelect==1:
        print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        for item in AllowedVehiclesList:
            print(item)
    elif menuSelect == 2:
        search_vehicle = input("******************************************\nPlease Enter the full Vehicle name: ")
        if search_vehicle in AllowedVehiclesList:
            print(f"{search_vehicle} is an authorized vehicle.")
        else:
            print(f"{search_vehicle} is not an authorized vehicle. If you received this in error, please check the spelling and try again.")
        
        continue #This was added to make the menu reappear unless 3 is pressed
    elif menuSelect == 3:
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        break  # Exit the loop and end the program
    else:
        print("Invalid input. Please try again.")

