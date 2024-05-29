# DELETE the elements lesser than 100
data = [4, 5, 104, 101, 111, 113, 107, 109, 100, 107, 114]
print('Before deletion :{}'.format(data))

stop = 0
for index, value in enumerate(data):
    print(f'Values : {value}')
    if value > 10:
        stop = index
        break
print(f'Stop: {stop}')
del data[:stop]
print("After deletion :{}".format(data))
print()