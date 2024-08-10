'''
Create a program that calculates the area of a room
- prompt the user for the length and width of the room in feet
- Display the area in both square feet and meters

What is the length of the room in feet?
What is the width of the room in feet?
You entered dimension of 15 feet by 25 feet
The area is?
300 square feet
27.871 square meters
'''
def get_numeric_input(prompt):
    while True:
        try:
            # Prompt the user for input and attempt to convert it to a float
            return float(input(prompt))
        except ValueError:
            # If conversion fails, inform the user and repeat the loop
            print("Invalid input. Please enter a numeric value.")

length = get_numeric_input("What is the length of the room in feet?\n")
width = get_numeric_input("What is the width of the room in feet?\n")
print(f'You entered dimensions of {length} feet by {width} feet.')
area = length * width
CONVERSION = 0.09290304
meters = area * CONVERSION
print("The area is:")
print(f"{area} square feet")
print(f"{meters} square meters")

# Create a new verison of the program that allows you to choose feet or meters for your inputs
def get_numeric_input(prompt):
    while True:
        try:
            # Prompt the user for input and attempt to convert it to a float
            return float(input(prompt))
        except ValueError:
            # If conversion fails, inform the user and repeat the loop
            print("Invalid input. Please enter a numeric value.")
            
def calculate_area(length, width, unit):
    if unit.lower() == 'feet':
        area = length * width
        print("The area is:")
        print(f"{area} square feet")
    elif unit.lower() == 'meters':
        area = length * width
        print("The area is:")
        print(f"{area} square meters")
    else:
        print("Not a recognised unit")
        
calculate_area(15, 20, 'meters')
    
        