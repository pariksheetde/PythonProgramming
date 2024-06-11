# WRITE A PALIDROME FUNCTION TO CHECK IF THE REVERSE STRING WORKS
# SOME OF THE EXAMPLES OF PALIDROMES ARE (RACECAR, MADAM)
def is_palidrome(string):
    """
    This Function is used to check if a word suplied by the user is palidrome.
    Palidrome means that a word read from backword will be same as the actual word
    """
    if str.casefold(string) == str.casefold(string[::-1]):
        print("\'{}\' is a palidrome".format(string))
    else:
        print("\'{}\' is not a palidrome".format(string))

prompt = input("Enter a word to check if the word is palidrome: ")
is_palidrome(prompt)
print()

def is_sentence_palidrome(string):
    """
    This Function is used to check if a sentence suplied by the user is palidrome.
    Palidrome means that a word read from backword will be same as the actual word
    """
    string = ""
    for char in string:
        if char.isalnum():
            string += char
    print(string)
    return str.casefold(string) == str.casefold(string[::-1])


word = input("Enter a sentence to check if the word is palidrome: ")
if is_sentence_palidrome(word):
    print('{} is a palidrome'.format(word))
else:
    print('{} is not a palidrome'.format(word))

print(is_palidrome.__doc__)
print(is_sentence_palidrome.__doc__)
help(is_palidrome)
help(is_sentence_palidrome)    