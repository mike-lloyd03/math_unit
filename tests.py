from math_unit import Unit

x = Unit(5, 'in-s')
y = Unit('5 ft-hr')
print(x, x.unit_type)
print(y, y.unit_type)
