# Problem
Inputs:
- None

Outputs:
- Robot Name: str

Rules:
- Same robot name cannot be used twice:
    - Assuming that if there is a name that was previously wiped, it CAN be reused
- Name can be wiped and new one generated after factory settings
- Generated names must be completely random

- Name follows the format of : 2 uppercase letters, followed by 3 digits
- - ??? random.seed ? - do we need to use it in the Robot ?

# Examples / Test Cases
- Robot class
    - constructor creates new name and assigns it to `name` variable
    - `name` property?
    - `reset()` method that generates new name and replaces it in the instance

# Data Structures
- Strings for names
- Probably a collection as class variable that stores all the used names
- strings for different characters of the

# Algorithm
Constructor:
[*] 1. Generate a new random name
2. If the name is in the list of taken names, keep generating other names.
3. Assign the name to the `name` **property**
4. Add the name to the list of taken names (class level)

Reset:
1. Remove the current name from the list of taken names
[*] 2. Generate a new random name
3. If the name is in the list of taken names, keep generating other names.
4. Assign the name to the `name` property
5. Add the new name to the list of taken names (class level)

[*] Name generator helper function
1. Create an empty 'result' string
(
2. Randomly select an uppercase character from A to Z.
3. Append it to the result
): Repeat 2 times

(
4. Randomly select a character between '1' and '9'
5. Append it to the result

) : Repeat 3 times
Return the result string


# Implem Notes
- while name in used_names: keep generating new name
- for each of 5 characters generate a choice
- constructor and reset can use a common helper method that generates the name
- Use 'name' property so that we use setter in both reset and constructor
    - As part of setter, add the name to the list of used names