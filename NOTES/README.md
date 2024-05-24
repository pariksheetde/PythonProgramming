1.  PYTHON IS DYNAMICALLY TYPED PROGRAMMING LANGUAGE
2.  Shared References : This is where variables share same area in memory, they share same object
3.  Everything in PYTHON is object like variables, functions, class are all objects
4.  Storing and retreiving data from memory / heap is taken care by python memory management.
    age = 10
5.  When we declare a variable, age, it becomes a reference to an object at the memory location. So variables in python are always
    references to the object in the memory. So variables are just memory addresses.
6.  Reference Counting : When multiple variables are assigned to each other, say for example
                                age = 10
                                marks = 10
both age and marks are assigned to same memory address. So same memory address will have 2 objects, age and marks. When one of the variable or both the variables are descoped, those memory address will be later reused by python programming. This is called reference counting. This process is taken care by python.
7.  