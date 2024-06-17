rand = [10, 20, 30, 40, True, False, 'Python']
# create empty list
tech_stacks = []
marks = list()

print(f'Type :{type(rand)}')
print(f'Type :{type(tech_stacks)}')
print(f'Type :{type(marks)}')

# print last element
print(f'Last Element: {rand[-1]}')
print(f'Last Element: {rand[len(rand) - 1]}')

tech_stacks.append('SQL')
tech_stacks.append('Azure Databricks')
tech_stacks.append('Azure Synapse')
print(tech_stacks)
print()
