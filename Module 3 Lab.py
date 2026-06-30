# ------------------------------------------------------------
# Name: Mahlet Ayenew
# Course: SDEV 265 System Software Analysis
# Module 3 Lab - Case Study: Lists, Functions, and Classes
# Date: June 29, 2026
#
# Description:
# This program demonstrates inheritance by creating a Vehicle
# superclass and an Automobile subclass. The program asks the
# user for information about a car and displays the information
# in a readable format.
# ------------------------------------------------------------

# Superclass
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


# Subclass
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print("\nVehicle Information")
        print("---------------------------")
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")


def main():
    print("Vehicle Information Program")
    print()

    vehicle_type = "car"

    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")

    # Validate number of doors
    while True:
        doors = input("Enter the number of doors (2 or 4): ")
        if doors in ("2", "4"):
            break
        print("Invalid input. Please enter 2 or 4.")

    # Validate roof type
    while True:
        roof = input("Enter the roof type (solid or sun roof): ").lower()
        if roof in ("solid", "sun roof"):
            break
        print("Invalid input. Please enter 'solid' or 'sun roof'.")

    car = Automobile(vehicle_type, year, make, model, doors, roof)

    car.display_info()


if __name__ == "__main__":
    main()