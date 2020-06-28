from math_unit import Unit

x = Unit('5 in/s')
# y = Unit('5 ft-hr')
print(x, x.numerator)
# print(y, y.unit_type)

# import re
# regex = r'(?P<val>^\d*\.*\d*)|(?P<num>(?<!/)\w+)|(?P<den>(?<=/)\w+)'
# test = '5.56 mm'
# print(re.findall(regex, test))
