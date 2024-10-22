class Clock:
    ONE_DAY = 1440

    def __init__(self, hours, minutes):
        self._hours = hours
        self._minutes = minutes

    @classmethod
    def at(cls, hours, minutes=0):
        return Clock(hours, minutes)

    def __str__(self):
        return f'{self._hours:02d}:{self._minutes:02d}'

    def __add__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        current_min = self._hours * 60 + self._minutes

        result_min = (current_min + other) % Clock.ONE_DAY

        new_hours, new_min = divmod(result_min, 60)
        return Clock.at(new_hours, new_min)

    def __sub__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        return self.__add__(-other)

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