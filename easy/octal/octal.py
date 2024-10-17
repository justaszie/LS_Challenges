import re

class Octal:
    def __init__(self, octal):
        self._octal = octal

    def _is_valid_octal(self):
        valid_pattern = r'^[0-7]+$'

        return (isinstance(self._octal, str)
                and re.search(valid_pattern, self._octal))

    def to_decimal(self):
        if not self._is_valid_octal():
            return 0

        digits = [int(char) for char in self._octal[::-1]]
        result = 0

        for power, digit in enumerate(digits):
            result += digit * 8**power

        return result