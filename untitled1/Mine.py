name = input("What is your name")
print(" ")

print("Hello, " + name)
car = input("What is the base price of the car?")
car = float(car)
print(" ")

tax = float(.0625 * car)
print("The taxes are 6.25% and are: ")
print(tax)
print(" ")

license = float(.025 * car)
print("The license fees are 2.5% and are: ")
print(license)
print(" ")

dealer_prep = int(325)
print("Dealer prep is: ")
print(dealer_prep)
print(" ")

destination = float(250.95)
print("Destination fees are: ")
print(destination)
print(" ")

print(name + ", the base price of your car is:")
print(car)
print(" ")

print(name + ", and the total cost you will pay for the car is:")
total = (car + tax + license + dealer_prep + destination)
print(total)

print(" ")

# input("\n\nPress the enter key to exit.")