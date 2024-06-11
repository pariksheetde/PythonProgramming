def is_sentence_palidrome(string: str) -> bool:
    string = ""
    for char in string:
        if char.isalnum():
            string += char
    print(string)
    return str.casefold(string) == str.casefold(string[::-1])


word = input('Enter a word to check: ')
if is_sentence_palidrome(word):
    print('{} is a palidrome'.format(word))
else:
    print('{} is not a palidrome'.format(word))