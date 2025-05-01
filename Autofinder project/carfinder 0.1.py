AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
print("******************************************\n    Autocountry Vehicle Finder v0.1    \n******************************************\nPlease Enter the following number below from the following menu:\n\n1.PRINT all authorized vehicles\n2. Exit")

menuSelect=int(input())
if menuSelect==1:
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for item in AllowedVehiclesList:
        print(item)
elif menuSelect==2:
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
    quit()