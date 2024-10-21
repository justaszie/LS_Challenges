class Clock:
    def __init__(self, hours, minutes):
        self._hours = hours
        self._minutes = minutes

    @classmethod
    def at(cls, hours, minutes=0):
        return Clock(hours, minutes)

    @staticmethod
    def pad_zeroes(number):
           return str(number) if number >= 10 else f'0{number}'

    def __str__(self):
        return f'{Clock.pad_zeroes(self._hours)}:' \
        f'{Clock.pad_zeroes(self._minutes)}'

    def __add__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        min_to_add = other % 1440
        current_min = self._hours * 60 + self._minutes
        result_min = current_min + min_to_add
        result_min %= 1440
        new_hours, new_min = divmod(result_min, 60)
        return Clock.at(new_hours, new_min)

    def __sub__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        min_to_subtract = other % 1440
        current_min = self._hours * 60 + self._minutes
        result_min = current_min - min_to_subtract
        if result_min < 0:
            result_min = 1440 + result_min
        new_hours, new_min = divmod(result_min, 60)
        return Clock.at(new_hours, new_min)

    def __eq__(self, other):
        if not isinstance(other, Clock):
            return NotImplemented

        return self._hours == other._hours \
        and self._minutes == other._minutes


if __name__ == '__main__':
    # print(Clock.at(23, 25) + 70)
    print(Clock.at(10, 30) + 60)
    print((Clock.at(2, 5) - 185) == Clock.at(23))
    print(Clock.at(2, 5) == Clock.at(2,5))