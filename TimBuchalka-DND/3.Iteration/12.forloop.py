numbers = "9,223,372,036,845,775,807"
generated_numbers = "".join(numbers)
print(generated_numbers)
lst_generated_numbers = generated_numbers.split(",")
print(lst_generated_numbers)

# METHOD 1
# CREATE A LIST OF NUMBERS FROM THE ABOVE STRING
int_generated_numbers = []
for indx in lst_generated_numbers:
    int_generated_numbers.append(int(indx))
print(f'Integer based list : {int_generated_numbers}')