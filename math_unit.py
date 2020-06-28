import re
from unit_list import unit_list

class Unit:
    def __init__(self, input_str):
        # if isinstance(num_str, str):
        #     self.value = float(re.match(r'^\d+', num_str)[0])
        # else:
        #     self.value = float(num_str)
        # self.unit = re.findall(r'[a-zA-Z]+', unit or num_str)
        self.value, self.numerator, self.denominator = self._parser(input_str)
        # try:
        #     self.unit_type = [unit_list[unit]['type'] for unit in self.unit]
        # except  KeyError:
        #     raise TypeError('The specified unit is not recognized.')

    def _parser(self, input_str):
        parse_re = r'(?P<val>^\d*\.*\d*)|(?P<num>(?<!/)\w+)|(?P<den>(?<=/)\w+)'
        res = re.findall(parse_re, input_str)
        numerators = []
        denominators = []
        for match in res:
            if match[0]:
                number = match[0]
            elif match[1]:
                numerators.append(match[1])
            elif match[2]:
                denominators.append(match[2])
        return (number, numerators, denominators)



    def __str__(self):
        return f'{self.value} {self.numerator}, {self.denominator}'


    # def __repr__(self):
    #     return self.__str__()


    def __add__(self, addend):
        if self.unit_type == addend.unit_type:
            return Unit(self.value + addend.convert(self.unit).value, self.unit)
        else:
            raise TypeError('The two values do not have matching unit types for addition')


    def __sub__(self, subtrahend):
        if self.unit_type == subtrahend.unit_type:
            return Unit(self.value - subtrahend.convert(self.unit).value, self.unit)
        else:
            raise TypeError('The two values do not have matching unit types for subtraction')


    def convert(self, to_unit: str, inplace=False):
        '''
        Converts the current unit to the specified unit

        Returns:
        A new Unit which has been converted to the specified unit.
        If the 'inplace' argument is set to True, it will convert the
        current unit to the specified unit and return itself
        '''
        if inplace:
            self.value = self.value / unit_list[self.unit]['mult'] * unit_list[to_unit]['mult'],
            self.unit = to_unit
            return self
        else:
            return Unit(self.value / unit_list[self.unit]['mult'] * unit_list[to_unit]['mult'], to_unit)
