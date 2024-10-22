# Problem
Input
- Month number (1-12) : int
- Year: int
- Descriptor of day - e.g. {first Monday}:
    1: quantifier: str  {first', 'second', 'third', 'fourth', 'fifth', 'last', and 'teenth'}
    2: day name: str {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', and 'Sunday'}

Output
- Date


Rules:
- Typically, meetups happen monthly on the same day of the week. E.g.:
    The first Monday of January 2021
    The third Tuesday of December 2020
    The last Thursday of January 2021
    ?? The teenth Wednesday of December 2020

- Construct objects that represent a meetup date
- ??? object should be able to determine the exact date of the meeting in the specified month and year E.g.
    - if you ask for the 2nd Wednesday of May 2021, the object should be able to determine that the meetup for that month will occur on the 12th of May, 2021.
    ??? - where do we get the "2nd Wednesday" from
- Descriptor - quantifier of day: str
    - {first', 'second', 'third', 'fourth', 'fifth', 'last', and 'teenth'}
    - Case is not important
- Descriptor - day name is a str {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', and 'Sunday'}
    - Case is not important
- Regarding the 'teeth'day, every month has exactly one "teenth" Monday, one "teenth" Tuesday

-ASSUMPTIONS:
    -

# Examples / Test Cases
- We will need `Meetup` class
    - Cnstructor that takes `year`, `month` arguments
    - `day()` method:
        - takes `weekday_name`, `weekday_quantifier` arguments
        - returns a `date` object from `datetime` module

- No input validation for constructor, nor for the day() methd

# Data Structures
- integers for year and month
- Strings for day descriptor: weekday name and quantifier
- date class objects returned by day() method


# Algorithm
Constructor:
    - take year and month as arguments
    - store them as instance variables

`day()` method:
[*] 1. Get all the days (day number) within the month that match the weekday input (e.g. all Mondays)
2. If the quantifier is NOT 'teenth':
    A. If the quantifier is last, select the last element in the collection
    B. Else, select the i-th element from the collection (based on starting index 1)
3. If the quanitifer is 'teenth' :
    A. Select the first day from the collection that is between 11 and 19 (inclusive)
3. Create a date object based on the selected day, input month and year.
4. Return the date object.


[*] To get all days that match the weekday input:
1. Iterate over each date in the month [**]
2. If the date matches the input weekday, [***] add it to collection of weekdays.


# Implem Notes
[***] 1. Dict that maps the input weekday name to its weekday number as defined in `date` class (1-7)
[**]  2. Create a date on 1st of the month, add 1 day (timedelta) to iterate. Stop iteration when the month changes.