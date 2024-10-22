# Problem
Input:

Output:

Rules:
- Build Custom Set Type class
- It should behave like a set of unique elements that can be manipulated in several well defined ways
- Elements of set will be numbers


# Examples / Test Cases
- `CustomSet` class:
DONE
- `is_empty(self)` instance method. Returns True if set is empty
    - constructor.
        - Arguments:
            - Either no arguments, or:
            - List of numbers
        - Ignores duplicates in the argument list. [1, 2, 2, 1] will create a set with 1 and 2.
    - `contains(self, number)` instance method. Returns True if the number is in set
    - `__eq__` : returns True if both sets contain the same elements (is_same)
      - `add(self, number)` method:
        - Add the number to the set (if not yet present)
        - If already present in the set, ignore
- `is_same(self, other_set)` instance method:
        - Returns True if both have exact same elements (no more, no less), no matter the order of the elements that were given in the list to the constructor.
- `is_subset(self, larger_custom_set)` instance method.
        - Returns true if all the elements of self are included in the `larger_custom_set`
        - If the instance (self) is an empty set, return True (any set, even empty set includes empty subset)
    - `is_disjoint(self, other_set)` instance method
        - If both instance and argument are empty sets, returns True
        - One empty, other non- empty, returns True
        - Otherwise, returns True if there are NO shared elements between 2 sets. No elements of `self` are present in the `other_set`

    - `intersection(self, other_set)`:
        - Return the elements of self that are present in other_set
        - Return empty set if no shared elements
            - If both sets are empty, the return is still empty set


    - `difference(self, other_set)` method:
        - 2 empty sets: return empty set (no different elements)
        - Return all elements of self that are not in other_set
            - IMPORTANT: order is important.
                - if self is empty and other set is set(1,2,3) = no elements = empty set
                - if self is non empty and other is empty = all elements of self

    - `union(self, other_set)` method:
        - 2 empty sets: return empty set
        - return new set that contains distinct elements from self and other set (no duplicates)



# Data Structures
- Elements stored are numbers
- Custom sets are created from lists of numbers (even for 1 number, we pass a list of 1 element)
- We will use lists to store the members
-



# Algorithms
Constructor:
1. Create an empty list and assign it to self._members
2. If a list was passed as arguments, iterate over each member. For each member:
    A. If the member is not in the list assigned to `members` instance variable, add the member to the list

`is_empty(self)`
1. Return true if the members instance variable points to an empty list

`contains(self, number)`
1. Iterate over each element in the `members` list. If a member matches the number argument, return True.

`add(self, number)`
1. If the number is not yet in `members`, append it to `members`

`is_same` / `__eq__()`:
1. If the `members` of both sets don't have the same length, return False. Else, continue:
2. Iterate over each element of self.members. If the member is not present in the `other.members`, return False.
3. If we reach the end, return True.

`is_subset(self, other_set)`
is_subset(self, larger_custom_set)` instance method.
        - Returns true if all the elements of self are included in the `larger_custom_set`
        - If the instance (self) is an empty set, return True (any set, even empty set includes empty subset)

1. Iterate over each element of `self.members`. If all elements are present in `other_set.members`, return True


`difference(self, other_set)`:
1. Create an empty custom set "result"
2. Iterate over members of self. For each member, if it's not present in other_set members, add it to the result set
3. Return the result set.




`union(self, other_set)`:
1. Create an empty custom set "result'
2. Set value of result.members to a copy of self.members
3. Collect all elements from other_set.members that are not in result.members and assign them to 'new_members' variable
4. Add members of new_members to result.members one by one



# Implem Notes