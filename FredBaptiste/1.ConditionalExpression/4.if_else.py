price = 300
if price <= 250:
    print(f"Purchase the product")
else:
    print(f"It's little expensive")
print('Done!')
print()

cost = 1250
if cost >= 1000:
    if cost >= 1750:
        print("Definately out of budget")
    elif cost >= 1001 and cost <= 1749:
        print('I will try to manage because the product is premium')
else:
    print("I will buy")
print('Done!')
print()

exp = 1000
if exp <= 1000:
    print("I will purchase")
else:
    if exp >= 2000 and exp <= 2500:
        print("Contact the vendor")
    else:
        print("Get new vendor")
print('Done!')
print()