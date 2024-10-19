# Problem
Input:
- a letter: str

Output:
- print out a diamond shape with the input letter at the widest point
- no return value

Rules:
- [ASSUMPTION] we are working with uppercase letters only
- First row contains 1 'A'
- Last row contains 1 'A'
- All rows, except the first and last, have exactly two identical letters. E.g:
    - B B
    C    C
    etc..
- ??? Diamond is horizontally and vertically symetric
- Width = height

- The shape is formed of uppercase letter characters : ??? Which letters? just As and input letter?
- Top half of diamond has increasingly wider rows
- Bottom half has increasingly narrower rows
- ??? Four corners (containing spaces) are triangles
- Diamond height is dynamic. The height depends on the input letter.
    - 'A': height = 1
    - 'C': height = length(A,B,C,B,A) = 5
    - 'F': height = length(A,B,C,D,E  F E,D,C,B,A) = 5 * 2 + 1

**Height Formula** Height = letters[A-input_letter] (excl) * 2 + 1.

- The rows are constructed:
    1. For each character from A to the input_letter (incl.)
        - Build a row of width = height.
        - Row is composed of :
            - N spaces: **Formula**
                - Row A = (height - 1 char) / 2
                - Row B to input letter: decrease by 1
                - Input letter - 1 to Row A: increase by 1
            - followed by the row character
            - X spaces: **Formula**
                - Row A: 0
                - Rows B to B (other end) = width - 2 chars - (N spaces * 2)
            - followed by the row character (except Rows A)
            - N spaces
            - Line end character '\n'


# Examples / Test Cases
We will need a `Diamond` class.
It has one class or static method `make_diamond()` that takes the letter input and returns a string with the diamond shape.

`answer = Diamond.make_diamond('A')`

# Data Structures
We'll Strings for letters. We'll work on their integer unicode point values so that we can work with ranges of characters from A to input letter.


# Algorithm
- First and last lines are special so we'll have separate logic to construct them
- diamond for just 'A' is special because it's just one row. so we'll separate the logic to create it.

Main logic:
1. If the letter is A:
    - return just one row 'A\n'
2. Calculate height / width of the diamond = `number of letters between 'A' and the input letter (exclusive) * 2 + 1`
3. Calculate the starting value for surrounding left and right spaces. Formula is `(height - 1 char) / 2`
4. Create empty "result" string
[*] 5. Iterate over the range of letters from 'A' to the input letter (incl.). On each iteration:
    A. Append the "surrounding spaces" number of spaces to the result string
    B. Append the current character value to the string
    C. If the current character is 'A':
        i. Append "surrounding spaces" number of spaces to the result string
    D. if the current character is not 'A':
        i. Calculate "between character spaces" value = `height - 2 chars - (surrounding spaces * 2)`
        ii. Append "between character spaces" number of spaces to the result string
        ii. Append "surrounding spaces" number of spaces to the result string
    E. append end of line character '\n' to the result string
    D. Decrease surrounding spaces value by 1
[**] 6. Iterate over the range of letters from letter before the input letter down to 'A', going downwards. On each iteration:
    Build the row using the same logic. Except surrounding spaces value should increase by 1.




[*] Iterating through the letters going upwards

[**] (e.g. 'B' if input letter was 'C')






# Implem Notes
Use unicode point values that represent the letters to iterate through a range of letters



 ??? spaces are calculated:
            - N spaces (on left and right):
                Example: Letter 'E'. Height = 9
                    - Row A. Start: (height - 1 char) / 2 = 4 on left and right
                    - Row B: 3
                    - Row C: 2
                    - Row D: 1
                    - Row E: 0
                    - Row D: 1
                    ...
                Logic:  Start with (height - 1 char) / 2. On each row until the input letter, it decreases by 1, then it increases by 1
            - X spaces
                - First row = 0
                - 2nd Row = .

                Example: Letter C. Height, width = A,B * 2 + 1 = 5
                    - Row A:
                        N spaces = (5 - 1) / 2 = 2
                        X spaces = 0

                    - Row B
                        N = 1
                        X spaces = 5 - 2 - 2 = 1

                    - Row C
                        N = 0
                        X spaces = 5 -2 - 0 = 3


                A = 0
                B =


        Example: letter 'E'. Height = (A,B,C,D) * 2 + 1 = 9
        For 'A': total width 9 - 1 char = 8 spaces, divided equally
        For 'B': Total width 9 - 2 char = 7 spaces, divided equally (??)
        For 'C': 9 - 2 = 7 spaces, divided equally
        For 'D': 9 - 2 = 7 spaces, divided equally


    2. For each character from (input-letter - 1) to A (incl.)

    - - The widest row has {height} characters (incl. spaces)

