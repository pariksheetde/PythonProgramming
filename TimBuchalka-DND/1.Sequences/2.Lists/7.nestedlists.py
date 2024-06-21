menu = [['egg', 'bacon'], 
        ['egg', 'sausage', 'bacon'], 
        ['egg', 'spam'], 
        ['egg', 'bacon', 'spam'],
        ['egg', 'bacon', 'sausage','spam'],
        ['spam', 'bacon', 'sausage', 'spam'],
        ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'],
        ['spam', 'sausage', 'spam', 'bacon', 'spam', 'tomato', 'spam']
        ]
for meal in menu:
    for index in range(len(meal) -1, -1, -1):
        if meal[index] == "spam":
            del meal[index]              
    print("Meals that contains \"spam\" to be deleted {}".format(meal))

print()

menu = [['egg', 'bacon'], 
        ['egg', 'sausage', 'bacon'], 
        ['egg', 'spam'], 
        ['egg', 'bacon', 'spam'],
        ['egg', 'bacon', 'sausage','spam'],
        ['spam', 'bacon', 'sausage', 'spam'],
        ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'],
        ['spam', 'sausage', 'spam', 'bacon', 'spam', 'tomato', 'spam']
        ]
for food in menu:
    for item in food:
        if item != "spam":
            print(item, end=" ")

    print()