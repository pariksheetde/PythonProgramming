class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    
box = Rectangle(10, 7.13)
print(f'Area of my box: {box.length * box.width}')