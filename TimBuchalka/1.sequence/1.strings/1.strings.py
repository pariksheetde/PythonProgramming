result = "Correct"
anaother_result = result
print(f'ID of Result: {id(result)}')
print(f'ID of Another Result: {id(anaother_result)}')
if id(result) == id(anaother_result):
    print("Woh! The address is same")
else:
    print("Hmm!. The address didn't match")

print()

delta = True
anaother_delta = delta
print(f'ID of Delta: {id(delta)}')
print(f'ID of Another Delta: {id(anaother_delta)}')
if id(delta) == id(anaother_delta):
    print("Woh! The address is same")
else:
    print("Hmm!. The address didn't match")

print()