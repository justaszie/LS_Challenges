# Problem
### Input
- Word: str
- List of anagrams: list of str


### Output
- Sublist of anagrams that contain the correct anagrams from input list for the input word: list of str

### Rules
- Anagram definition here: a string that can be produced by re-arranging the characters in the input word
    - same length
    - all characters of input word are present in the resulting word the same amount of times
    - does NOT equal original word (is not the same word as original)
- Case insensitive
- No anagrams matches returns an empty list
- Input validation: None

- Checksum ???

# Examples / Test Cases


# Data Structures
- Anagram class
    - initializer that takes the input word as argument
    - match(candidates) instance method that takes a list argument and returns a list of anagrams

# Algorithm
- Initializer:
    1. Store the input word
    2. Count the frequency of each character (counting case insensitive) and store it in the instance

- match method:
    1. Create an empty list "results"
    2. Iterate over each string in the list of strings passed as argument. For each string "candidate":
        1. Count the frequency of each character (counting case insensitive) in the candidate
        2. If the characters and their frequencies are the same as those of the input word, add the candidate to the results list
    3. Return the results list

# Implem notes
- generate a dict mapping of character counts for the input word and for each anagram candidate.
    The dicts must be equal for the candidate to qualify.
-