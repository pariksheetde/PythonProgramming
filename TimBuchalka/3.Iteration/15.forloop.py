# CONVERT THE STRING OF NUMBERS INTO INTEGERS OF LIST
# SOLUTION 1
numbers = "1,123,056,789,321,654,987"
splitted_numbers = numbers.split(",")
print(f'Original Values: {splitted_numbers}')
also = []
for num in splitted_numbers:
    also.append(int(num))
print(f'After converting to Integer: {also}')
print()

# CONVERT THE STRING OF NUMBERS INTO INTEGERS OF LIST USING LIST COMPREHENSION
# SOLUTION 2
number = "1,123,056,789,321,654,987"
numbers_splitted = [int(item) for item in number.split(",")]
print(f'After converting to Integer: {numbers_splitted}')
print()