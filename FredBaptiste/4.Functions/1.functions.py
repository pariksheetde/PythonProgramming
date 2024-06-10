# WRITE A PALIDROME FUNCTION TO CHECK IF THE REVERSE STRING WORKS
# SOME OF THE EXAMPLES OF PALIDROMES ARE (RACECAR, MADAM)
def is_palidrome(string):
    if str.casefold(string) == str.casefold(string[::-1]):
        print("\'{}\' is a palidrome".format(string))
    else:
        print("\'{}\' is not a palidrome".format(string))

prompt = input("Enter a word to check if the word is palidrome: ")
is_palidrome(prompt)
print()

def is_sentence_palidrome(string):
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