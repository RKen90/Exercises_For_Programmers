'''
Create a program that:
- Determines how many years you have left until retirement and the year you can retire
- prompt for your current age
- prompt for the age you want to retire

What is your current age?
At what age would you like to retire?
You have X years left until you can retire
It's 2015 so you can reture in 2055
'''

year = 2024
age = int(input("What is your current age?\n"))
retirement_age = int(input("At what age would you like to retire?\n"))

years = retirement_age - age
print(f'You have {years} years left until you can retire.')
year_retired = year + years
print(f'It\'s {year} so you can retire in {year_retired}')

# Handle dituations where the program returns a negative number by stating the user can already retir

year = 2024
age = int(input("What is your current age?\n"))
retirement_age = int(input("At what age would you like to retire?\n"))

if retirement_age <= age:
    print("You can already retire")
else:
    print(f'You have {years} years left until you can retire.')
    year_retired = year + years
    print(f'It\'s {year} so you can retire in {year_retired}')