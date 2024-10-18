# Problem
Inputs
- 0 or more non-negative integers

Output:
- String with one or more verses of the song

Rules:
- The return value consists of verses in a single string, separated by a line feed character (\n)

- The arguments can be (a, b) where (a, b) is a range of decreasing numbers. We generate a verse for each number between a and b, incl.
- ASSUMPTION: the input is limited to 2 values:
    - if no values, we generate the whole song (verses for numbers 99 to 0)
    - if 1 value, we generate 1 verse
    - if 2 values, we generated a verse for each number in the range a->b

- The integer arguments will range from 0 to 99 (incl).
    - From test cases, the assumption is that we don't verify the input

Verse structure:
- Each verse has 2 lines that include dynamic values based on input. For input N:
    - Line 1: "{N} bottles of beer on the wall, {N} bottles of beer.\n"
    - Line 2: "Take one down and pass it around, {N-1} bottles of beer on the wall.\n"

    - Special cases for these input values:
        - 1:
            - Line 1 follows the same structure
            - Line 2: "Take it down and pass it around, no more bottles of beer on the wall"
        - 0:
            - Line 1: "No more bottles of beer on the wall, no more bottles of beer.\n"
            - Line 2: "Go to the store and buy some more, 99 bottles of beer on the wall.\n"

- The 2 lines in each verse are separated by LF character \n

# Examples / Test Cases
We will need:
- a `BeerSong` class.
    - `verse()` method. It takes 0, 1, or 2 arguments and generates and returns verses

Most likely helper method to generate one verse with an int argument.

Cover edge cases:
- verse for 0
- verse for 1

cover 2 input scenario: range of numbers

cover single input scenario: verse for 1 number

# Data Structures
- inputs are all integers
- outputs are in a single string
- Probably use lists for different verses to be included, that we'll join into a single string


# Algorithms

0. Create an empty list "verses"
1. If no arguments are passed, set variables:
    - to = 0
    - from = 99
2. If one argument is passed, set variables:
    - from = argument
    - to = argument
3. If 2 arguments are passed, et variables:
    - from = argument_1
    - to = argument_2

4. Iterate over integer values "verse_number" from the "from" value to "to" value (both included), going downwards. For each verse_number value:
    [*] A. Generate a verse for the current number value
    B. Add the verse to the verses list

5. Join the verses in the "verses" list into a single string, separated by '\n' characters


[*] Verse generation helper method:
Takes 1 integer input N:

1. If N == 0:
    - set line_1 variable = "No more bottles of beer on the wall, no more bottles of beer.\n"
    - set line_2 variable = "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
2. Else:
    - set line_1 variable = "{N} bottles of beer on the wall, {N} bottles of beer.\n"
    if N == 1:
        - set line_2 variable = "Take it down and pass it around, no more bottles of beer on the wall"
    else:
        - set line_2 variable = "Take one down and pass it around, {N-1} bottles of beer on the wall.\n"
3. Concatenate lines line_1 and line_2 into "verse" string variable
4. Return the verse

# Implem Notes
Default arguments for verse() method : both default to None to make them optional.
If they are none, the method will set some values.


# Mistake & Correction
There are in fact 3 class methods, not 1:
    - `verses()` that takes 2 arguments for a range of numbers
    - `verse()` that takes 1 argument
    - `lyrics()` that takes 0 arguments and generates the whole song

verses calls verse() N times for each value in range
lyrics calls verse() N times for the whole range 99-0