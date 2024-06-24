panagram = """The quick brown fox
jumps \tover the 
lazy dog"""
words = panagram.split()
print(words)
print()

numbers = "1,123,056,789,321,654,987"
splitted_numbers = numbers.split(",")
print(f'Original Values: {splitted_numbers}')
also = []
for num in splitted_numbers:
    also.append(int(num))
print(f'After converting to Integer: {also}')
print()

# JOIN CREATES STRING FROM SEQUENCE. SPLIT ON THE OTHER HAND SPLIT THE STRING AND CREATE A LIST 
generated_list = [
    '9', ' ', '',
    '2', '2', '3', ' ',
    '3', '7', '2', ' ',
    '0', '3', '6', ' ',
]
print("".join(generated_list).split(" "))
print()