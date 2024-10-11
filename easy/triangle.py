"""
Algorithm:
    1. Initializer takes 3 arguments and assigns them to a, b, c sides
        - If any value is <= 0 raise valueerror
        - If a + b <= c or a + c <= b or b + c <= a
    2. kind property dynamically returns the type based on the sides values:
        1. If a == b and b == c, return "equilateral"
        2. Else, if a==b or b==c or a==c, return "isosceles"
        3. Else, return "scalene"
"""

# --- V1: using 3 variables --
# class Triangle:
#     def __init__(self, a, b, c):
#         if a <= 0 or b <= 0 or c <= 0:
#             raise ValueError('Sides cannot be 0 or negative')
#         if (a + b) <= c or (a + c) <= b or (b + c) <= a:
#             raise ValueError('Sum of 2 sides must always be longer than the third side')

#         self.a, self.b, self.c = (a, b, c)

#     @property
#     def kind(self):
#         a, b, c = (self.a, self.b, self.c)

#         if a == b and b == c:
#             return 'equilateral'
#         if a == b or b == c or a == c:
#             return 'isosceles'

#         return 'scalene'

#  --- V2: using a list ---
class Triangle:
    def __init__(self, a, b, c):
        self.sides = (a, b, c)

        if any(side <= 0 for side in self.sides):
            raise ValueError('Sides cannot be 0 or negative')
        if (a + b) <= c or (a + c) <= b or (b + c) <= a:
            raise ValueError('Sum of 2 sides must always'
                             ' be longer than the third side')


    @property
    def kind(self):
        a, b, c = self.sides
        if a == b and b == c:
            return 'equilateral'
        if a == b or b == c or a == c:
            return 'isosceles'
        return 'scalene'

if __name__ == '__main__':
    test_triangle = Triangle(1, 1, 3)