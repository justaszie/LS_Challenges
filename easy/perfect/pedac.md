# Problem
### Inputs
- positive number: int

### Outputs
- Classification: str. {'perfect', 'abundant', 'deficient'}


### Rules
- classification: abundant, perfect, or deficient
    - Based on comparison between the _number_ and the (_sum of its positive divisors_) - aka _Aliquot sum_.
    - Positive divisor of a = positive number "divisor" where a % divisor == 0 and divisor is not a
    - **Perfect number** = aliquot sum == number
    - **Abundant** = aliquot sum > number
    - **Deficient** = aliquot sum < number

- Assumption that 0 should not be allowed as input


# Examples / Test Cases
We will need:
- a class `PerfectNumber`
- a class method `classify()`. It takes and integer and returns its classification among possible values: {'perfect', 'abundant', 'deficient'}

- Negative number input should raise an exception (ValueError) with a specific error message "Input must be a positive integer". Assuming same goes for 0 input

- Test cases check one case for each classification


# Data Structures
- `PerfectNumber` class with a class method `classify`.
- Input is an int
- Output is a string: one of 3 pre-defined values: {'perfect', 'abundant', 'deficient'}

# Algorithm
1. if the input number is less or equal to 0, return a ValueError with the message "Input must be a positive integer". Else, continue.
[*] 2. Calculate the Aliquot sum of the number
3. Compare the aliquot sum to the input number:
    A. If sum == number, return 'perfect'
    B. if sum > number, return 'abundant'
    C. if sum < number, return 'deficient'

* Calculating the Aliquot sum, given input number:
1. Create empty divisors list
2. Iterate through divisor candidates from 1 up to the input number(excl). For each candidate
    3. If input number % current candidate == 0, append divisors list
4. Calculate the sum of the numbers in the divisors list.
5. Return the sum