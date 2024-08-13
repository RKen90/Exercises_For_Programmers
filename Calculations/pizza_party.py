'''
Write a program to eenly divide pizza
- Prompt for the number of people
- Prompt for the number of pizzas
- Prompt for the number of slices per pizza

Ensure the number of slices comes out even

- Display the number of pieces each person should get
- If there are leftovers show the number 
'''

num_people = int(input("How many people?\n"))
num_pizzas = int(input("How many pizzas?\n"))
num_slices = num_people // num_pizzas
leftover = 0

if num_slices % 2 == 0:
    print(f"{num_people} with {num_pizzas}")
    print(f"Each person gets {num_slices} slices of pizza")
    print(f"There are {leftover} leftover pieces")
else:
    while num_slices % 2 != 0:
        num_slices -= 1
        leftover += 1
        print(f"{num_people} with {num_pizzas}")
        print(f"Each person gets {num_slices} slices of pizza")
        print(f"There are {leftover} leftover pieces")
    

