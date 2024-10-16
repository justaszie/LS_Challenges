class PerfectNumber:

    @staticmethod
    def _aliquot_sum(number):
        divisors = [ candidate for candidate in range(1, number)
                     if number % candidate == 0 ]
        return sum(divisors)

    @classmethod
    def classify(cls, number):
        if number <= 0:
            raise ValueError("Input must be a positive integer")

        aliquot_sum = cls._aliquot_sum(number)
        if aliquot_sum == number:
            return 'perfect'
        elif aliquot_sum > number:
            return 'abundant'
        else:
            return 'deficient'
