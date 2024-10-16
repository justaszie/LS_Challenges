# Problem
### Inputs
1. Word: str

### Outputs
1. Scrabble score for the word: int

## Rules
- Score for the word = the sum of values of each letter
- Values of letters are provided below. Only the characters in this table give points. Any other character is 0 pts.
- If input is not valid (e.g. empty string, None, whitespaces), return 0
- Assumption: we don't verify if it's a valid word
- Assumption: matching against the letter values table is case insensitive

L'e'tter	Value
{
('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'):  1,
('D', 'G'):  2,
('B', 'C', 'M', 'P'):  3,
('F', 'H', 'V', 'W', 'Y'):  4,
('K'):  5,
('J', 'X'):  8,
('Q', 'Z'):  10,
}


# Examples / Test Cases
We will need `Scrabble` class:
    - initializer method that takes the input word as argument and stores it
    - `score()` instance method that returns the score for the stored word

Test cases include various invalid inputs, one letter inputs, lowercase and uppercase words. Everything that is a valid string is concidered a valid word.

## Mistake - oversight
There was another class method: calculate_score in the test suite that  missed

# Data Structures
- Input is string
- Output is integer
- Scrabble class:
    - initializer method
    - method variable to store the word
    - score method that calculates and returns integer score value
    - Most likely, a constant mapping for letter values:
    {('A', 'E', 'I' ....) : 1,
        ('D', 'G')
    }

# Algorithm
1. Create a letter value mapping list_letters : score
2. Add it to class constants

Initializer:
    - Store the input word in uppercase

Score method
1. Set result integer to 0
2. Iterate over the stored input word. For each character:
    A. Iterate over each list of letters in the value mapping. For each list of letters:
        i. if current character is in the list, add the vlaue of the list to the result
3. Return the result integer


# Implem Notes
{
('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'):  1,
('D', 'G'):  2,
('B', 'C', 'M', 'P'):  3,
('F', 'H', 'V', 'W', 'Y'):  4,
('K'):  5,
('J', 'X'):  8,
('Q', 'Z'):  10,
}