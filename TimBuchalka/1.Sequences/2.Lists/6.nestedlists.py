menu = [['egg', 'bacon'], 
        ['egg', 'sausage', 'bacon'], 
        ['egg', 'spam'], 
        ['egg', 'bacon', 'spam'],
        ['egg', 'bacon', 'sausage','spam'],
        ['spam', 'bacon', 'sausage', 'spam'],
        ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'],
        ['spam', 'sausage', 'spam', 'bacon', 'spam', 'tomato', 'spam']
        ]

# Return those list that doesn't contain "spam" in their menu
for meal in menu:
    if "spam" not in meal:
        print(f'Meal that doesn\'t contain \"spam\": {meal}')
        # Return the count of "spam" in each meal
    else:
        print(f'{meal} has "spam" score of {meal.count("spam")}')
print()