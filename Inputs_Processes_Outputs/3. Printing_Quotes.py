'''
Create a program that prompts for a quote and an author.
Display the quotation and author

e.g.
What is the quote? These arent the droids your'e looking for
Who says is? Obi-Wan Kenobi
Obi-Wan Kenobi say, "These arent the droids you're looking for!"

Here are some common escape sequences:

\' - Single quote
\" - Double quote
\\ - Backslash
\n - Newline
\t - Tab
\r - Carriage return
\b - Backspace
'''
# V1 - How I would do it
quote = input("What is the quote?\n")
name = input("Who said it?\n")
print(f'{name} says, "{quote}"')

# V2 - Using escape characters
quote = input("What is the quote?\n")
name = input("Who said it?\n")
print(f"{name} says, \"{quote}\"")
