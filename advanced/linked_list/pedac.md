# Problem
Inputs


Outputs


Rules
- Each object in Linked List contains:
    - data
    - "next" field pointing to next object in the list
- Lists can contain ranges of data (e.g. numbers 1-10)
- Linked List must have methods to reverse itself (last element becomes first, second to last becomes second, etc.)
- Linked List must have a methods to:
    - Convert itself to a simple list
    - Create linked list from a simple list
??? - Linked list itself should contain the pointer to the first element




# Examples / Test Cases
- Element Class:
    - Constructor that takes:
        - First argument: the data to be stored in the 1st element
        - 2nd argument (optional): object instance of the previous element.
            - If this is provided, the element passed in this instance gets its `next` set to the new instance.
    - `datum` variable (property?)
    - `next` variable (property?)
        - element that is next in list
        - if there is no next, returns None __(i.e. by default, `next` is None )__
    - `is_tail()` that returns True / False if the element is last in the list
        - returns True if the list has only 1 element

- `SimpleLinkedList` class:





    - `reverse()` method:
        - revert the order. last element becomes first, first becomes last. e.g 1 -> 2 -> 3 becomes
        3 -> 2 -> 1


    - `is_empty()` method: returns boolean
    - `head` variable. Contains the first element in the list (instance of `Element`)
    - `push` method, that takes one argument: data element
        ??? - adds the element to the beginning of the list (the head of the list)
     - Constructor that takes no arguments
    - `size` variable (property)
        - 0 for empty lists
     - `peek()` method. Takes no arguments and returns:
        - the data stored in the first element (head) in the list (the actual data )
        - returns None if the list is empty
     - `pop()` method. Takes no arguments. Returns the data at the START of the list (not the element, the actual datum). Removes the entry too (`next` becomes the head)
     - `from_list()` method that creates a Linked List from a simple list
        - Accomodate for:
            - Empty List: creates empty linked list
            - None: creates empty linked list
            - Non-empty list (normal scenario). For a list [1, 2, 3], 1 will be the head, next will be 2, etc.
    -  `to_list()` method.
        - If empty linked list: return []
        - If non-empty, return a list [a -> b] where a is the first element of the linked list and b is the last
# Data Structures


# Algorithms
--- ELEMENT ----
Constructor:
 - takes 2 arguments: datum(mandatory), previous(optional):
1. Assign datum value to datum instance var
2. Set next value to None
3. If previous is provided:
    A. Reassign the `next` value of the previous element to the current element


`is_tail()`
1. Return True if `next` value of the element is None. Else, return 'False'

---- LINKED LIST -----
Constructor:
1. Take no arguments and set the head of the list to None

`head` variable:
1. Return the element that is assigned to `head` variable

`is_empty()` method:
2. Return true if `head` is assigned to None, otherwise false

`push(data)` method:
1. Create a new `Element` instance by sending the input data and the current `head` element to the constructor.
2. Reassign list's `head` to the new element

`size()` method:
1. set counter to 0
2. Assign 'head' to temporary 'current_element' value
3. while the `current_element.next` is not None:
    A. increment counter by 1:
    B. reassign current_element to current_element.next
4. Return counter value

`reverse()`method:
1. Convert the current linked list to simple list
2. Reverse the simple list
3. Return a new linked list object from the reverted list

Alternative:
-

# Implem Notes