# Problem
Inputs:
1) A string of digits
2) Length of the number series to return

Outputs:
List of series of consecutive numbers of specified length, created from the input string of digits

Rules:
- 0 is also treated as other digits
- For lenght = N, we generate and return all possible consecutive number series of length N
- - Output is a list of sublists where each sublist is a series of length N.
- If input length N is greater than the length of the string, throw a `ValueError` exception
- From test cases, the assumption is we don't validate the format of the input string
- Consecutive numbers means: numbers that appear one after the other in the input string (NOT in their numeric order)
- Repeated numbers in the input string are treated as separate numbers






# Examples / Test Cases
We will need a `Series` class. The class has:
    - constructor that takes a string of digits
    - `slices()` instance method that returns a list of sublistsm that contain series of consecutive numbers of length N specified as input to the method.

# Data Structures
string for the input
list of lists where the nested lists contain the number series
the elements in the nested lists are numbers (convert str to number)

# Algorithm
Series constructor:
1. Take a string input and assign it to an instance variable

Slices method:
1. If length input > length of instance variable string, raise a ValueError. Else, continue.
2. Create an empty list "result"
3. Iterate through index values from 0 up to (length of string - length of series), inclusive. For each index value:
    A. Take a slice of string for indexes: current index TO current index + length of series (exclusive).
    B. Create an empty list "sublist"
    C. Iterate over the slice. For each character of the slice:
        i. Convert the character to integer
        ii. Append the integer to sublist list
    D. Append the sublist value tothe "result" list
4. Return the "result" list


String: "03243"
Index | Number
0       0
1       3
2       2
3       4
4       3

Lenght = 2
Iterate over the number:
Index: 0

Take elements 0 - 1 (incl.) [0:2]

Index: 1
Take elements 1 - 2 (incl.) [1:3]

Index: 2
Take elements 2 - 3 (incl.) [2:3]

Index: 3
Take elements 3 - 4 (incl.) [3:5]

Index: 4
STOP

The last index should be (len(string) - series_length).

Length = 3
Idx 0: [0:3]
Idx 1:  [1:4]
Idx 2:  [2:5]




# Implem Notes