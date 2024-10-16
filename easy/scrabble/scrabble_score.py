class Scrabble:
    VALUES = {
        ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'):  1,
        ('D', 'G'):  2,
        ('B', 'C', 'M', 'P'):  3,
        ('F', 'H', 'V', 'W', 'Y'):  4,
        ('K'):  5,
        ('J', 'X'):  8,
        ('Q', 'Z'):  10,
        }

    def __init__(self, word):
        self._word = word

    # V1 - static method doing most of the work
    # @staticmethod
    # def calculate_score(word):
    #     result = 0
    #     if word and isinstance(word, str):
    #         for char in word.upper():
    #             for letters in Scrabble.VALUES.keys():
    #                 if char in letters:
    #                     result += Scrabble.VALUES.get(letters)

    #     return result

    # def score(self):
    #     return Scrabble.calculate_score(self._word)

    # V2 - instane method doing most of the work
    @classmethod
    def calculate_score(cls, word):
        return cls(word).score()

    def score(self):

        # V2.a : normal looping
        # result = 0
        # if self._word and isinstance(self._word, str):
        #     :
        #         for letters in :
        #             if char in letters:
        #                 result += Scrabble.VALUES.get(letters)
        # return result

        # V2.b: comprehension
        if not self._word or not isinstance(self._word, str):
            return 0

        return sum([ value
                     for char in self._word.upper()
                     for letters, value in Scrabble.VALUES.items()
                     if char in letters ])
