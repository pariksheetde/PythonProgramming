def is_palidrome(string):
    return str.casefold(string) == str.casefold(string[::-1])


word = input('Enter a word to check: ')
if is_palidrome(word):
    print('{} is a palidrome'.format(word))
else:
    print('{} is not a palidrome'.format(word))