# WRITE A PALIDROME FUNCTION TO CHECK IF THE REVERSE STRING WORKS
def is_palidrome(string):
    if str.casefold(string) == str.casefold(string[::-1]):
        print("{} is a palidrome".format(string))
    else:
        print("{} is not a palidrome".format(string))

prompt = input("Enter a word to check if the word is palidrome: ")
is_palidrome(prompt)
print()