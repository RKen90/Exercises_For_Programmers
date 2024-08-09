'''
Write a program that:
- prompts for two numbers
- print the sum
- print the difference
- print the product
- print the quotient
'''

num1 = input("Please enter your first number\n")
num2 = input("Please enter your second number\n")
num1 = int(num1)
num2 = int(num2)

# Mathematical sums
additions = num1 + num2
subtraction = num1 + num2
multi = num1 * num2
div = num1 / num2

# Output
print(f'{num1} + {num2} = {additions}')
print(f'{num1} - {num2} = {subtraction}')
print(f'{num1} * {num2} = {multi}')
print(f'{num1} / {num2} = {div}')


'''
Revisions
- Ensure the inputs are entered as numeric values
'''

num3 = input("Please enter your first number\n")
num4 = input("Please enter your second number\n")
proceed = False

try:
    num3 = float(num3)
    num4 = float(num4)
    proceed = True
except ValueError:
    print("Please enter a numeric value")
    proceed = False

while proceed == True:    
    print("Calculating")
    additions = num3 + num4
    subtraction = num3 - num4
    multi = num3 * num4
    div = num3 / num4 
    print(f'{num3} + {num4} = {additions}')
    print(f'{num3} - {num4} = {subtraction}')
    print(f'{num3} * {num4} = {multi}')
    print(f'{num3} / {num4} = {div}')
    proceed = False