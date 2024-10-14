"""
DATA STRUCTURES
    - DNA class:
        - initializer:
            - Input: DNA string value
        - hamming_distance() instance method:
            - Input: DNA string value to compare against
            - Output: Hamming distance value: int

ALGORITHM
1. Initialize DNA with a DNA strand string value
2. Calculate and return output by calling the instance method hamming_distance:

Details on (2):
1. Set the result value to 0
2. Compare the lengths of the instance variable string and the method input string:
    A. If the lengths are equal, set the upper_limit value to length of instance variable string
    B. If the instance var string is shorter, set the upper limit to length of instance var
    C. If the instance var is longer, set the upper limit to length of input var
3. Iterate through index integer values from 0 to upper_limit (excl). For each value:
    A. Compare the characters at the current index value on both strings:
        i. if the characters are unequal, increment result value by 1
4. Return the result value
"""

class DNA:
    def __init__(self, strand):
        self._strand = strand

    def hamming_distance(self, other_strand):
        result = 0

        # V1 - Simple iterations

        # instance_len = len(self._strand)
        # other_len = len(other_strand)
        # if instance_len <= other_len:
        #     limit = instance_len
        # elif instance_len > other_len:
        #     limit = other_len

        # for idx in range(limit):
        #     if self._strand[idx] != other_strand[idx]:
        #         result += 1

        # V2 - using zip(). It stops iterating once the shorter iterable is exhausted
        # for char1, char2 in zip(self._strand, other_strand):
        #     if char1 != char2:
        #         result += 1

        # V3 - one liner with comprehension
        return sum([ 1 for char1, char2 in zip(self._strand, other_strand) if char1 != char2 ])

        return result