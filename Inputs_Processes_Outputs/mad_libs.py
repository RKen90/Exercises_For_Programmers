'''
Create a simple mad-lib program that:
- prompts the user for a noun
- prompts the user for a verb
- prompts the user for a adverb
- prompts the user for a adjective

- injects those into a story you create
'''
'''
noun = input("Please enter \"Mirna\", \"Robert\" or \"George\"\n")
verb = input("Please enter a verb\n")
adjective = input("Please enter an adjective\n")
adverb = input("Please enter an adverb\n")

print(f"The {adjective} cat {adverb} {verb} up the {noun}")
'''

# Implement a branching story where the questions determine how the story is constructed`
noun = input("Please enter \"Mountain\", \"Tree\" or \"House\"\n")
verb = input("Please enter a verb\n")
adjective = input("Please enter an adjective\n")
adverb = input("Please enter an adverb\n")

if noun.lower() == "mountain":
    print(f"The {adjective} Mirna {adverb} {verb} up the {noun}")
elif noun.lower() == "house":
    print(f"The {adjective} Robert {adverb} {verb} in the {noun}")
elif noun.lower() == "tree":
    print(f"The {adjective} George {adverb} {verb} up the {noun}")
else:
    print("Word not recognised")

