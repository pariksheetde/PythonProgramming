menu = [['egg', 'bacon'], 
        ['egg', 'sausage', 'bacon'], 
        ['egg', 'spam'], 
        ['egg', 'bacon', 'spam'],
        ['egg', 'bacon', 'sausage','spam'],
        ['spam', 'bacon', 'sausage', 'spam'],
        ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'],
        ['spam', 'sausage', 'spam', 'bacon', 'spam', 'tomato', 'spam']
        ]

# write a logic to delete `spam` from the list
# solution 1
for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == 'spam':
            del meal[index]
    print(" ".join(meal) ,sep=", ")

print()

# solution 2
for meal in menu:
    for item in meal:
        if item != 'spam':
            print(item, end=", ")

print()