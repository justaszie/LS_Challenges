class SumOfMultiples:
    def __init__(self, *args):
        self._numbers_set = set(args) if args else {3, 5}

    def _is_multiple(self, multiple_candidate):
        return any([multiple_candidate % set_number == 0
                    for set_number
                    in self._numbers_set])

    def to(self, limit_number):
        multiples = {multiple_candidate for multiple_candidate
                     in range(1, limit_number)
                     if self._is_multiple(multiple_candidate)}

        return sum(multiples)

    @classmethod
    def sum_up_to(cls, limit_number):
        return cls().to(limit_number)

if __name__ == '__main__':
    print(SumOfMultiples(4, 4).to(15))



