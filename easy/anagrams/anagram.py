class Anagram:
    @staticmethod
    def get_character_counts(word):
        return {char: word.casefold().count(char) for char in set(word.casefold())}

    def __init__(self, word):
        self._word = word.casefold()
        self._character_counts = Anagram.get_character_counts(word)

    def _is_anagram(self, candidate):
        return (Anagram.get_character_counts(candidate)
                == self._character_counts
        and self._word.casefold() != candidate.casefold()
        )

    def match(self, candidates):
        return [ candidate for candidate in candidates
                if  self._is_anagram(candidate)]


if __name__ == '__main__':
    test_ana = Anagram('Orchestra')
    print(test_ana.match(["cashregister", "Carthorse", "radishes"]))
