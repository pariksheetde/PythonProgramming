menu = [['egg', 'bacon'], 
        ['egg', 'sausage', 'bacon'], 
        ['egg', 'spam'], 
        ['egg', 'bacon', 'spam'],
        ['egg', 'bacon', 'sausage','spam'],
        ['spam', 'bacon', 'sausage', 'spam'],
        ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'],
        ['spam', 'sausage', 'spam', 'bacon', 'spam', 'tomato', 'spam'],
        ]

# DISPLAY ONLY THE ELEMENTS THAT HAS NO "SPAM"
for meal in menu:
    if 'spam' not in meal:
        print(f'Menu that has no "spam" {meal}')
print()
# DISPLAY ONLY THE ELEMENTS THAT HAS "SPAM"
for meal in menu:
    if 'spam' in meal:
        print(f'Menu that has "spam" {meal}')
print()

# DISPLAY THE COUNT THAT HAS "SPAM"
for meal in menu:
    if 'spam' in meal:
        print(f'Menu that has "spam" {meal} has a score of {meal.count("spam")}')
print()