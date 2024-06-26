flowers_shrubs = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Flower",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Liliac - Shrub",
    "Mangolia - Shrub"
]
flower = []
shrub = []
for garden in flowers_shrubs:
    if 'Shrub' in garden:
        shrub.append(garden)
    elif 'Flower' in garden:
        flower.append(garden)
print(f'Shrub: {shrub}')
print(f'Flower: {flower}')

print()