grade = 40

if grade >= 90:
    print(f"Excellent")
elif grade >= 80 and grade <= 89:
    print(f"Good score")
elif grade >= 70 and grade <= 79:
    print(f"Average score")
elif grade >= 60 and grade <= 69:
    print(f"Below par score")
elif grade >= 50 and grade <= 59:
    print(f"Very bad performance")
else:
    print("FAIL")
print()