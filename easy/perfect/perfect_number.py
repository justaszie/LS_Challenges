class PerfectNumber:

    @classmethod
    def aliquot_sum(cls, number):
        return sum([ candidate for candidate in range(1, number)
                     if number % candidate == 0 ])

    @classmethod
    def classify(cls, number):
        if number <= 0:
            raise ValueError("Input must be a positive integer")

        aliquot_sum = cls.aliquot_sum(number)
        if aliquot_sum == number:
            return 'perfect'
        elif aliquot_sum > number:
            return 'abundant'
        else:
            return 'deficient'
