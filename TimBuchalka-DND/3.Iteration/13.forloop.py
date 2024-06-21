user_input = input("Enter 3 numbers of your choice, separated by comma: ")
numbers = user_input.split(",")

token = []
for user_token in numbers:
    token.append(int(user_token))
    print(token)

num_1, num_2, num_3 = token
result = (num_1 + num_2 - num_3)
print(f'The result of adding {num_1} + {num_2} - {num_3}: {result}')