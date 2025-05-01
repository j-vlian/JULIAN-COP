import os

AllowedVehiclesList = [
    'Ford F-150',
    'Chevrolet Silverado',
    'Tesla CyberTruck',
    'Toyota Tundra',
    'Rivian R1T',
    'Ram 1500'
]

FILENAME = "allowed_vehicles.txt"

# Initialize file if file doesn't exist
def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as file:
            for vehicle in AllowedVehiclesList:
                file.write(vehicle + "\n")
def load_vehicles():
    with open(FILENAME, "r") as file:
        return [line.strip() for line in file.readlines()]

# Save vehicles back to file
def save_vehicles(vehicle_list):
    with open(FILENAME, "w") as file:
        for vehicle in vehicle_list:
            file.write(vehicle + "\n")
initialize_file()

while True: #main loop
    AllowedVehiclesList = load_vehicles()

    print("******************************************\n    AutoCountry Vehicle Finder v0.5    \n******************************************\nPlease Enter the following number below from the following menu:\n\n1. PRINT all Authorized Vehicles\n2. SEARCH for Authorized Vehicle\n3. ADD Authorized Vehicle\n4. DELETE Authorized Vehicle\n5. Exit\n******************************************")

    try:
        menuSelect = int(input())
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 5.")
        continue

    if menuSelect == 1:
        print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        for item in AllowedVehiclesList:
            print(item)

    elif menuSelect == 2:
        search_vehicle = input("******************************************\nPlease Enter the full Vehicle name: ")
        if search_vehicle in AllowedVehiclesList:
            print(f"{search_vehicle} is an authorized vehicle.")
        else:
            print(f"{search_vehicle} is not an authorized vehicle. If you received this in error, please check the spelling and try again.")

    elif menuSelect == 3:
        new_vehicle = input("******************************************\nPlease Enter the full Vehicle name you would like to add: ")
        AllowedVehiclesList.append(new_vehicle)
        save_vehicles(AllowedVehiclesList)
        print(f'You have added "{new_vehicle}" as an authorized vehicle.')

    elif menuSelect == 4:
        del_vehicle = input("******************************************\nPlease Enter the full Vehicle name you would like to REMOVE: ")
        if del_vehicle in AllowedVehiclesList:
            confirm = input(f'Are you sure you want to remove "{del_vehicle}" from the Authorized Vehicles List?\n').lower()
            if confirm == 'yes':
                AllowedVehiclesList.remove(del_vehicle)
                save_vehicles(AllowedVehiclesList)
                print(f'You have REMOVED "{del_vehicle}" as an authorized vehicle.')
            elif confirm == 'no':
                continue
            else:
                print("Invalid response. Returning to main menu.")
        else:
            print(f'"{del_vehicle}" was not found in the authorized vehicle list.')

    elif menuSelect == 5:
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        break
    else:
        print("Invalid input. Please try again.")
