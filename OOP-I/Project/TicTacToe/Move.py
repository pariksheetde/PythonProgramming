class Move:

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
    
    def is_valid(self):
        if self._value >= 1 and self._value <= 9:
            return 1
        else:
            return 0
        
    def get_rows(self):
        if self._value in (1, 2, 3):
            return 0  ## 1st row
        elif self._value in (4, 5, 6):
            return 1  ## 2nd row
        elif self._value in (7, 8, 9):
            return 2  ## 3rd row
        
    def get_columns(self):
        if self._value in (1, 4, 7):
            return 0  ## 1st column
        elif self._value in (2, 5, 8):
            return 1  ## 2nd column
        elif self._value in (3, 6, 9):
            return 2  ## 3rd column

"""
# Define an instance of class, Move 
mv = Move(3)
print(f'Initial Value: {mv.value}')

mv.is_valid()
print(f'{mv.is_valid()}')

print()

# Define an instance of class, Move 
lx = Move(8)
print(f'Row Index: {lx.get_rows()}')
print(f'Column Index: {lx.get_columns()}')
"""