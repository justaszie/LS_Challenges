# Problem
Octal to decimal conversion

### Inputs
- octal number: str

### Outputs
- octal converted to decimal: int

### Rules
- Invalid octal input returns 0
    - Input should be a string
    - The strign should only contain these digits: 0, 1, 2, 3, 4, 5, 6, 7. If it includes any other character, it's invalid and `to_decimal()` should return 0
- No validation is done or errors raised during initialization
- Decimal is digits multiplied by their appropriate power of 10 (starting with 0 from the right), summed up.
    E.g. 233 = 3 * 10^0 + 3 * 10^1 + 3 * 10^2
- Octal is same but powers of 8:
    E.g. 233 octal = 3 * 8^0 + 3 * 8^1 + 2 * 8^2 = 3 + 24 + 128 = 155
-

# Examples / Test Cases
We will need:
    - Octal class
        - initializer that takes the octal number __as string input__
        - to_decimal instance method that returns the value converted to decimal __as int__

We're testing the correctness of converted values and the fact that invalid value returns 0

# Data Structures
We will use strings to iterate over input characters, convert them to int to calculate base 8 values.


# Algorithm
Initializer:
    1. Take the str as input and assign it to instance variable

to_decimal() method
[*] 1. If the input is invalid return 0. Else, continue.
2. Set power variable to 0
3. Set result variable to 0
4. Iterate over each character of the input string, in reverse. For each character:
    A. Convert the current character to int value and assign to "digit" variable
    B. Calculate value = 10 ^ power * digit
    C. Increment the result by the value of "value" variable
    D. Increment the power by 1
5. Return result


* Helper method to check the input validity:
    1. If the input is not a string, return False
    2. If the string does not match the required pattern, return False (use regex)


# Implem Notes
- Invalid octal helper function:
    - use regex for fun: r'^[0-7]+$'