# Problem

### Inputs
- positive number: int
- set of 1 or more numbers: set
### Outputs
- sum of multiples of numbers in set that are less than the 1st input number


### Rules
- If the input set is not given, use set of {3, 5}
- ??? Validate that the 1st input is positive?
- Find the numbers up to the (1) 1st input (excl) that are multiples of any of the (2) numbers in the set input.
    - Remove duplicates
- Sum up the numbers that meet the criteria
- Assumming that we don't need to do any validation on either the number input or the set input

# Examples / Test Cases
We will need `SumOfMultiples` class. It includes:
    - Constructor that takes any number of positional arguments. These arguments represent the set of numbers (2nd input). It stores the set of numbers in a new instance.
    - class method `sum_up_to()` that takes 1 positive number as argument. This is the 1st input: number that defines the limit.
        - This method works without set argument - i.e. it works with default set of {3, 5}
    - instance method `to()` that takes 1 positive number as argument. This is the 1st input: number that defines the limit.
        - This method takes the set of numbers from the instance data.


# Data Structures
- `SumOfMultiples` class:
    - constructor
    - class method `sum_up_to()`
    - instance method `to()`

numbers that will be stored in a set
integers
most likely a set to store the unique multiples

# Algorithm
Constructor:
    - take any number of positional arguments (*args)
    - Store the numbers in a set

`sum_up_to()` class method:
    1. create numbers_set variable with {3, 5} value
    2. return the return value of calculate_sum() method by passing the set and the input_number argument

`to()` method:
    1. return the return value of calculate_sum() method by passing the set stored in the instance data and the input_number argument

`calculate_sum()` helper method
    1. initialize the "multiples" variable with an empty set
    2. iterate through integer values from 1 up to the input number (excl.). For each integer
        A. iterate over each number in the input numbers set. For each set number:
            i. if the current integer is a multiple of the current set number, add it to the "multiples" set
                - multiple means current_integer % set_number == 0
    3. calculate sum of the numbers in "multiples" set
    4. return the sum


# Implem notes
Common helper function `calculate_sum()` that calculates the sum for a given set and limit number. It will be used by both instance method and class method.


