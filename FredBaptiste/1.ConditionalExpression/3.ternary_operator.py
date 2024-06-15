rating = 2
CTC = 35_00_000

bonus = ((CTC * 30) / 100) if rating == 1 else ((CTC * 10) / 100)
hike = ((CTC * 8) / 100) if rating == 1 else ((CTC * 10) / 100)
print(f'Next CTC: {bonus + CTC + hike}')
print()
