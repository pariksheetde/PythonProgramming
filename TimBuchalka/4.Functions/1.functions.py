def is_palidrome(string):
    reverse_string = string[::-1]
    if str.casefold(reverse_string) == str.casefold(string):
        print(f'It\'s Palidrome')
    else:
        print(f'It\'s not palidrome')

is_palidrome('MAdAm')