from math_unit import Unit

x = Unit('1 mi')
y = Unit(2, 'km')
z = Unit(5, 's')

print('---Testing add, sub')
print(f'{x} + {y} =', x + y)
print(f'{x} - {y} =', x - y)
print(f'{x} + {z} = ', x + z)
print()
print('---Testing in place conversion---')
