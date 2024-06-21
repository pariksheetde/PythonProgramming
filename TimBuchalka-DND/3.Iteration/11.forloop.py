flowers = ['Daffodil',
           'Evening Primrose',
           'Iris',
           'Hydrangea',
           'Lavender',
           'Sunflower',
           'Tiger Lily'
        ]
separator = ","
print(separator.join(flowers))
print()

flowers = ['Daffodil',
           'Evening Primrose',
           'Iris',
           'Hydrangea',
           'Lavender',
           'Sunflower',
           'Tiger Lily'
        ]
fav = []
for flower in flowers:
    if flower.split(" "):
        fav.append(flower)
print(fav)