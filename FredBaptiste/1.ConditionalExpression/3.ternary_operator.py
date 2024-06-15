rating = 2
CTC = 35_00_000

bonus = ((CTC * 30) / 100) if rating == 1 else ((CTC * 10) / 100)
hike = ((CTC * 8) / 100) if rating == 1 else ((CTC * 10) / 100)
print(f'Next CTC: {bonus + CTC + hike}')
print()

a = 10
b = 0

result = a / b if b != 0 else None
print(f'Result of Ternary Operator: {result}')
print()

ask_price = 100

volume = 50 if ask_price > 50 else 80
print(f'Result of Ternary Operator: {volume}')
print()

current_value = 100
running_total = 15_000
running_count = 125

clean_value = -999 if current_value == -999 else current_value
print(f'Clean Value: {clean_value + current_value}')
print()