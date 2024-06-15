rating = 1
CTC = 35_00_000

bonus = ((CTC * 30) / 100) if rating else "Default"
hike = ((CTC * 8) / 100) if rating else "Default"
print(f'Next CTC: {bonus + CTC + hike}')
print()
