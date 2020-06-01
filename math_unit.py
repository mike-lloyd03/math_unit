import re
from unit_list import unit_list as ul

class Unit:
    def __init__(self, num_str, unit=None):
        if isinstance(num_str, str):
            self.value = float(re.match(r'^\d+', num_str)[0])
            self.unit = re.search(r'\w+$', num_str)[0]
        else:
            self.value = float(num_str)
            self.unit = unit

    def __str__(self):
        return f'{self.value} {self.unit}'

    def __repr__(self):
        return __str__()

    def __add__(self, new_unit):
        return Unit(self.value + new_unit.convert(self.unit).value, self.unit)

    def __sub__(self, new_unit):
        return Unit(self.value - new_unit.convert(self.unit).value, self.unit)
    
    def convert(self, to_unit: str, inplace=False):
        '''
        Converts the current unit to the specified unit

        Returns:
        A new Unit which has been converted to the specified unit.
        If the 'inplace' argument is set to True, it will convert the 
        current unit to the specified unit and return itself
        '''
        if inplace:
            self.value = self.value / ul[self.unit]['mult'] * ul[to_unit]['mult'], 
            self.unit = to_unit
            return self
        else:
            return Unit(self.value / ul[self.unit]['mult'] * ul[to_unit]['mult'], to_unit)
