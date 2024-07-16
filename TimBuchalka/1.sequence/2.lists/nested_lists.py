even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

lst = (even + odd)
print(f'After concatenation: {lst}')

nested_lst = (even, odd)
print(f"Creating Nested List: {nested_lst}")

print()

nsted_lst = [[2, 4, 6, 8], [1, 3, 5, 7, 9]]

for inner_list in nsted_lst:
    print(inner_list)

    for value in inner_list:
        print(value)

print()