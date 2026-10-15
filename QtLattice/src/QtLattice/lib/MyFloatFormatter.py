import re
from PyQt5.Qt import QRegExp, QRegExpValidator


class MyFloatFormatter:

    regex_number = r"\s*[-+]?(([1-9]+[0-9]*\.?[0-9]*)|([0]?\.[0-9]+)|0)\s*"
    regex_operation = fr"\s*\(?{regex_number}([-+*/]{regex_number}\)?\s*)*"
    regex_expression = fr"\s*\(?{regex_operation}(([-+/]|[*]{{2}}){regex_operation}\)?\s*)*"

    def __init__(self,
                 format: str = "16.10f",
                 precision: float = None,
                 limitation: float = None,
        ):
        self.setFormat(format)
        self.setPrecision(precision)
        self.setLimitation(limitation)
        self.validator = QRegExpValidator(
            QRegExp(MyFloatFormatter.regex_expression)
        )

    def setFormat(self, format):
        digits = list(map(int, re.findall(r'\d+', format)))
        self.format = format
        self.length = digits[0]
        self.resolution = digits[1]
        self.magnitude = digits[0]-2-digits[1]
        return self

    def setPrecision(self, precision: float = None):
        if precision is None:
            precision = 10**(-self.resolution)
        self.precision = precision
        return self

    def setLimitation(self, limitation: float = None):
        if limitation is None:
            limitation = 10**(self.magnitude) - 10**(-self.resolution)
        self.limitation = limitation
        return self

    def string_limitation(self):
        return self.float_to_string(-self.limitation)

    def string_to_float(self, text):
        value = round(eval(text), self.resolution)
        value = min(value, +self.limitation)
        value = max(value, -self.limitation)
        return value

    def float_to_string(self, value):
        value = min(value, +self.limitation)
        value = max(value, -self.limitation)
        text = format(value, self.format)
        return text

    def evaluate(self, input):
        if input.count('(') == input.count(')'):
            return self.string_to_float(input)
