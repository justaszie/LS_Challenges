class RomanNumeral:
    MAPPING = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
    }

    DIVISORS = sorted(MAPPING.keys())

    @staticmethod
    def get_largest_divisor(number):
        highest_index = max([idx for idx, divisor in enumerate(RomanNumeral.DIVISORS) if number // divisor >= 1])
        return highest_index, RomanNumeral.DIVISORS[highest_index]

    def __init__(self, number):
        self._number = number

    def to_roman(self):
        result = ''
        number = self._number

        while number > 0:
            divisor_idx, divisor  = self.__class__.get_largest_divisor(number)
            multiple = number // divisor

            if multiple > 1:
                if multiple == 4:
                    next_divisor = RomanNumeral.DIVISORS[divisor_idx + 1]
                    value = next_divisor - divisor
                    result += f"{RomanNumeral.MAPPING[divisor]}{RomanNumeral.MAPPING[next_divisor]}"

                else:
                    value = multiple * divisor
                    result += RomanNumeral.MAPPING[divisor] * multiple
            else:
                remainder = number % divisor
                previous_divisor = RomanNumeral.DIVISORS[divisor_idx - 1]

                if remainder >= 4 * previous_divisor:
                    next_divisor = RomanNumeral.DIVISORS[divisor_idx + 1]
                    value = next_divisor - previous_divisor
                    result += f"{RomanNumeral.MAPPING[previous_divisor]}{RomanNumeral.MAPPING[next_divisor]}"
                else:
                    value = divisor
                    result += f"{RomanNumeral.MAPPING[divisor]}"

            number -= value
        return result
