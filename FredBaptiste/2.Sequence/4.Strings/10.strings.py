# index() is used to find the index position of the specified value
# if the specified value is not found in the string, index() will raise exception
marks = [10, 15, 20, 25, 30, 35, 40, 45, 50]
print(f'40 is available at Index Position: {marks.index(40)}')
print()

msg = 'For every action there is equal and opposite reaction'
print(f'Word "action" can be found at Index Position: {msg.index("reaction".casefold())}')
print()

# index() is used to find the index position of the specified value
# if the specified value is not found in the string, find() will raise -1
msg = 'For every action there is equal and opposite reaction'
print(f'Word "total" can be found at Index Position: {msg.find("total".casefold())}')
print()

msg = 'For every action there is equal and opposite reaction'
print(f'Word "action" can be found at Index Position: {msg.find("reaction".casefold())}')
print()

print(f'Index Position for "10": {[10, 15, 20, 25, 30, 35, 40, 45, 50].index(10)}')
print(f'Index Position for "name": {"Whats in a name".index("name")}')
print(f'Index Position for "name": {"Whats in a name".find("enemy")}')
print()

# find index() position for multiple occurance of a particular string
stmt = 'For every action there is equal and opposite reaction'
# print(f'Word "action" can be found at Index Position: {msg.find("action".casefold())}')
print(f'Word "action" can be found at Index Position: {stmt.find("action".casefold(), int(stmt.find("action".casefold()) + len("action")))}')
print()

message = 'Imagination is more powerful than knowledge - Einstein'
print(f"'Einstein' is found at index position: {message.find('Einstein')}")
print('Einstein' in message)
print()