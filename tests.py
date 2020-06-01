from math_unit import Unit

x = Unit('1 mi')
y = Unit(2, 'km')

print('---Testing add, sub')
print(f'{x} + {y} =', x + y)
print(f'{x} - {y} =', x - y)
print()
print('---Testing in place conversion---')
