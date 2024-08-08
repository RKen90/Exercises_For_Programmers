import random

'''
Create a program that:
- prompts for your name 
- and prints a greeting using your name
'''

name = input("Hello, what is your name?\n")
print(f"Hello {name}, it is nice to meet you!")
      
''' 
Challenges
- Write a new version without using any variables
'''       

print("It is nice to meet you" + " " + input("What is your name?\n"))


#Write a version of the program that displays different greeting for different people

greetings = [
    "Hello",
    "Hi there",
    "Good morning",
    "Good afternoon",
    "Good evening",
    "Howdy",
    "Greetings",
    "Welcome"
]

name = input("Hello, what is your name?\n")
print(f"{random.choice(greetings)} {name}!, it is nice to meet you!")
      
