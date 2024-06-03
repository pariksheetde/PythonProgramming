# Python has 4 sequence types
''''
1. string
2. list
3. tuple
4. range
What's a sequence: Sequence is a ordered set of items.

'''
# format - STRING INTERPOLATION
age = 25
print('My age is {}'.format(age))

print()

print('There are {} days in {}, {}, {}, {}, {}, {}, {}'.format(31, 'January', 'March', 'May', 'July', 
                                                               'August', 'October', 'December'))
print()

print("Jan: {0}, Feb: {1}, Mar: {2}, Apr: {2}, May: {0}, Jun: {2}, \
Jul: {0}, Aug: {0}, Sep: {2}, Oct: {0}, Nov: {2}, Dec: {0} days".format(31, 29, 30))

print("""
      Jan: {0}
      Feb: {1}
      Mar: {2}
      Apr: {2}
      May: {0}
      Jun: {2}
      Jul: {0}
      Aug: {0}
      Sep: {2}
      Oct: {0}
      Nov: {2}
      Dec: {0} 
      """.format(31, 29, 30))
print()

print("PI is approximately :{}".format(22 / 7))
print("PI is approximately :{0:12f}".format(22 / 7))
print("PI is approximately :{0:12.50f}".format(22 / 7))
print("PI is approximately :{0:52.50f}".format(22 / 7))
print("PI is approximately :{0:62.50f}".format(22 / 7))
print("PI is approximately :{0:72.50f}".format(22 / 7))
print()