# age = int(input("Enter your age : "))
# print(f"I am {age} years old")
# if age < 18:
#     print("You are minor. Study properly")
# elif age >= 18 and age <=21:
#     print(f"I go to college")
# elif age >=21 and age <=25:
#     print(f"I am working professional")
    
print("--------------------------------------------------------------------------------------------------------------------------")

# age = float(input("What's you age? "))
# print(f"You have lived for {age * 12} months")

print("--------------------------------------------------------------------------------------------------------------------------")

age = int(input("Enter your age "))
is_adult = age >=18
if is_adult:
    print(f"You are adult")
elif age < 18:
    print(f"You are still minor")
elif age >=60:
    print(f"You are getting old")