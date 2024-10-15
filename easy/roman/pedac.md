# Problem
### Inputs

### Outputs
- Decimal Number (int)
- Roman number representation (str)

### Rules
- Maximum allowed input: 3000
- Roman Numbers:
I 1
V: 5,
X: 10,
L: 50,
C: 100,
D: 500
M: 1000

- Number in front of another number:  AB = B - A. E.g. IX = X - I = 10 - 1 = 9
- If decimal number N falls between 1 roman number and (another roman number - previous number), we repeat the lower number N times. E.g.
    - 3 is between I and IV, so we do I * 3.
    - But if it equals (larger number - smaller number), we use smaller before larger notation. 400 is D (500) - C (100) so we do CD instead


# Example / Test Cases
Provided test cases of various decimal numbers from 1 to 3000
No input validation tests

# Data Structures
RomanNumeral class:
    - initializer that stores the decimal number (int)
    - to_roman() instance method that returns a string that is the roman numeral


# Algorithm - Exploration

mapping = {
    1: 'I',
    5: 'V',
    10: 'X',
    ....
}


If remainder of (larger closest number)
EXAMPLE: 6
6 // 50 = 0
6 // 10 = 0
6 // 5 = 1 [STOP]
    - Add value[5] = 'V' to the string
    - Subtract 5 from the input
    - Repeat steps (divide until remainder found) for the remainder (1):
        - 1 // 5 = 0; 1 // 1 = 1
            - Add value[1] = 'I' to the string
            - subtract 1 from input
            - if input = 0: STOP

EXAMPLE: 8
8 // 50 = 0
8 // 10 = 0
8 // 5 = 1 [STOP]
    - IF 8 % 5 < (5 - 1):  add 'V' and continue
    - ELSE IF 9 % 5 < (5 - 1), add 'I' and add 'V'
    - Add  'V' to the string.
    - Input = 8 - 5 = 3
        - 3 // 1 = 1
            - Add 'I' to the string
                - input = 3 - 1 = 2:
                    2 // 1 = 2
                        ...







1. Create a "result" string and set to empty string
2. Create a dictionary of mapping decimal numbers to their roman letter representation: 1: 'I', 5: 'V', etc.
3. If the decimal number is a key in the mapping dictionary, append the corresponding value to the "result" string.
[*] 4. Else, If there is a pair of keys (i, i + 1) in the mapping dictionary, where decimal number = value[i + 1] - value[i], append the result string with value[i], then with value[i+1]
[**] 5. Else, if the number is

* detailed logic:
    1. iterate through sorted list of mapping
    2.


X. Return the "result" string



Example: 3
    1. not in the direct mapping
    2. not [*]
    3.

3 % 1 = 0
3 % 5 = 3
3 % 10 = 3


4 % 1 = 0
4 % 5 = 4
4 % 10 = 4

6 % 1 = 6

6 % 5 = 1
6 % 10 = 6

7 % 5 = 2
8 % 5 = 3
9 % 5 = 4

if (b - x) < 4:
    repeat a  * (b - x) times <- doesn't work.
else:
    'ab'

Divide a by 10 as long as a > 10 (?)

x = 6
- no division
- a sits between 5 and 10
- 10 is closest larger number (b)
- diff = 10 - 6 = 4
    -


a and b = numerals in the mapping
Keep dividing input x by numerals (true division) from biggest to smallest until x // a = 1
If remainder x % a < (b - a):
    - we set x = x - a
    - add numeral[a] to the string.

Else if remainder x % a == (b-a):
    - x = x - x
    - addd "numeral[a]numeral[b]" to the string

- continue the loop until a == 0

EXAMPLES:
    17:
- divide by 50 == 0
- divide by 10 == 1. STOP DIVIDING. Set a to 10
remainder 17 % 10 = 7.
    50 - 10 = 40.
    remainder 7 < 40:
    add numeral[a] = 'X' to the string
    input = 17 - 10 = 7

    7:
- divide by ...
- divide by 5 == 1. STOP DIVIDING. Set a to 5
remainder 7 % 5 = 2.
    5 - 1 = 4
    remainder 2 < 4:
    add numeral[a] = 'V' to the string
    input = 7 - 5 = 2

    2:
divide by ...
divide by 1 == 2. STOP DIVIDING. Set a tp 1
remainder 2 %% 1 = 2.
    5 - 1 = 4
    remainder 2 < 4:
    add 'I' to the string
    input = 2 - 1 = 1


Example 96:
    96 % 50 = 1
    b - a = 100 - 50 = 50
    96 % 50 = 46 < (b-a):
        add numeral[50] = 'L' to the string
        set input = 96 - 50 = 46


----------
8, 9

80, 90 :

(a, b): b is divisor, a is the value before divisor.
When I find the divisor. How many times do I need to repeat the smaller value. (Exception if divisor is 1, smaller value is also 1)
    - if < 4: we repeat the smaller value
    - if >= 4: we use "ab" notation

80 // 100 = 0
80 // 50 = 1
    80 % 50 = 30
        30 // 10 = 3

90 // 100 = 0
90 // 50 = 1
    90 % 50 = 40
        40 // 10 = 4



8 // 5 = 1. 5 is divisor
    8 % 5 = 3
        3 // 1 = 3:
            - we repeat 1 three times

9 // 5 = 1. 5 is divisor
    9 % 5 = 4
        4 // 1 = 4:
            - we use 'IV' notation.


If we have X where x // divisor > 1:
    - (divisor - smaller_divisor)


### Algorithm - Final solution that works

1. Until input is 0
1. find divisor.
2. If x // divisor > 1: (example: 420)
    if x // divisor = 4:
        - we do value = (bigger_divisor - divisor)
        - we add "value[divisor]value[bigger_divisor] to string
        - we set x = x - value
        - Continue
    else:
        - we do value = (x // divisor) * divisor
        - We add "value[divisor]" repeated (x // divisor) times to string
        - we set x = x - value
        - Continue
3. Else if x // divisor = 1 (example 92)
    - if x % divisor >= (4 * smaller_divisor):
        - we do value = (bigger_divisor - smaller_divisor)
        - we add "value[smaller_divisor]value[bigger_divisor] to string
        - we set x = x - value
        - Continue
    - else: (ex. 82)
        - we do value = divisor
        - we add "value[divisor]" to string
        - we set x = x - value
        - Continue

