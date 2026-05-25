from car import Car

cars = []

print("Welcome to the Vehicle Database")
print("You can enter your vehicle here.")
print("Type if 'q' you want to leave")

while True:
    model = input("Model: ")
    if model.lower() == "q":
        break
    year = input("Year: ")
    if year.lower() == "q":
        break
    color = input("Color: ")

    if color.lower() == "q":
        break
    try:
        car = Car(model, int(year), color)
        cars.append(car)
    except ValueError:
        print("Year must be a number")

if cars:
    show_database = input("Do you want to see the database? (y/n): ").lower()
    if show_database == "y":
        for x in cars:
            print(f"{x.model}, {x.year}, {x.color}")

print("Thank you for using the Vehicle Database")
