# Problem
Input
- Time:
    - mandatory hour in 24 hr format
    - optional minutes (1-60, incl)


Output
- clock objects that represent time


Rules
- Add / subtract minutes from the time represented by `Clock` instance
    - This should return a new `Clock` object
    - Only use arithmetic operations, no date/time functionality
- Compare `Clock` instances for equality (if they have same time, they are equal)
- The `Clock` instances can be converted to string of 'HH:MM' format

- Edge cases:
    - Take care of going backwards (e.g. midnight - 1) or 2am - 3
    - Wraping around after midinight (11:30 + 50)
    - Adding time that is > 1 day
    - 0 is midnight
- The hour input format is 24hr

- ASSUMPTION: there is no input validation required either to create clock object or add, subtract

-

# Examples
class method `Clock.at(h, m=0)` -> creates a `Clock` object with the time stored and returns it
`__str__()` method to return the time as string
`__add__()`, `__sub__()` methods to add / subtract time and return new objects


# Data Structures
Integers for hours and minutes
Strings as return values of __str__ that represent the time stored in the `Clock` instance
Integers for minutes to be added / subtracted


# Algorithm
--- `at()` method ---
- Takes 2 arguments:
    - mandatory number of hours as first argument
    - optional number of minutes as second argument (default value = 0)

1. Create an instance of `Clock` using the constructor method.
    - Pass the hours argument
    - Pass the minutes argument, if provided, else 0
2. Constructor creates the object with 2 instance values: `hours` and `minutes`

--- add method ---
1. Divide the time to add by 1440min (day), keep the remainder
2. Convert current time to minutes
3. Add the minutes to add (from step 1)
4. Divide the resulting time by 1440 min (day), keep the remainder
5. Convert minutes back to hours (current minutes // 60, current minutes % 60)
6. Create and return new clock object

--- subtract method ---
1. convert current time to minutes
2. divide (minutes to subtract) by 1440, keep remainder (takes care of day(s) scenario)
3. Subtract minutes from current time
    - If, the result time is negative, set current time = 1440 - absolute value of result
    - If the result is positive, current time = result
4. Convert current time back to hours,minutes.
5. Create and return new clock object

--- str method ---
1. If the hours value is > 10, convert hours to string
2. Else, convert hours to string and prepend it with a '0'
3. Repeat the same with minutes
4. Create a string "{hours}:{minutes}"
5. Return the string

### NOTES
1. ADD
 --- Normal cases ---
10:35 + 150 :
    * 10:35 = 635 mins
    * 635 + 150 mins = 785 mins
    * 785 divmod 60 = 13h, 05 mins

Solution:
1. convert current time to minutes
2. Add minutes
3. Convert back to hours (div for hours, mod for minutes)

--- Close to midnight: wrap around ---
11:30 + 50
    * 23:30 = 1410
    * 690min + 50 = 1460
    * time = 1460 // 1440 = 20mins past midnight

Solution:
1. Convert current time to minutes
2. Add minutes
3. Keep the remainder of time % 1440 (days)
4. Convert back to hours


--- Adding day(s) ----
24h * 60 mins = 1440 mins / day
Solution to cover day(s) scenario: time to add = time to add % 1440.

**OVERALL SOLUTION**


2. SUBTRACT
--- normal case --
1. convert to minutes
2. divide minutes to subtract by 1440, keep remainder
3. Subtract minutes
4. Convert back to hours,minutes.

-- negative wrap around, e.g. 00:30 - 50 --
30 min - 50 = -20 minutes.
If result is negative: calculate 1440 (midnight) - (abs valut of minutes)

03:45 - 300mins
225 mins - 300 mins = -75mins



# Implem Notes
TBC - represent hours as minutes?
Using remainders to count only minutes to add, even if the added time is days?
