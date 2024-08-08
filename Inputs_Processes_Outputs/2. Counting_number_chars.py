'''
Create a program that:
- prompts for an input string
- and displays output that shows the input string and the number of characters in the string
'''

sting_input = input("Please enter a string of your choice\n")
print(f'Your string, ({sting_input}), has {len(sting_input)} characters')

# If the user inputs nothing, state that the user must enter something
sting_input = input("Please enter a string of your choice\n")
if len(sting_input) == 0:
    print('User must input something!')
else:
    print(f'Your string, ({sting_input}), has {len(sting_input)} characters')
    
# Make it repeatable
complete = False

while complete != True:
    sting_input = input("Please enter a string of your choice\n")
    if len(sting_input) == 0:
        print('User must input something!')
    else:
        print(f'Your string, ({sting_input}), has {len(sting_input)} characters')
    again = input("Try again: Y/N?")
    if again.lower() == "n":
        complete = True