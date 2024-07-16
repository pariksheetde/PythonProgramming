menu = [['egg', 'bacon'], 
        ['egg', 'sausage', 'bacon'], 
        ['egg', 'spam'], 
        ['egg', 'bacon', 'spam'],
        ['egg', 'bacon', 'sausage','spam'],
        ['spam', 'bacon', 'sausage', 'spam'],
        ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'],
        ['spam', 'sausage', 'spam', 'bacon', 'spam', 'tomato', 'spam']
        ]

# rerurn those list where `spam` is in the menu
for meal in menu:
    if 'spam' in meal:
        print(f'"spam" has a score of {meal.count("spam")}: {meal}')
print()

# rerurn those list where `spam` is not in the menu
for meal in menu:
    if 'spam' not in meal:
        print(f'"No Spam": {meal}')