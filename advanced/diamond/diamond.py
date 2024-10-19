class Diamond:

    @staticmethod
    def make_one_row(width, character, surrounding_spaces):
        result = ' ' * surrounding_spaces
        result += character

        if character != 'A':
            between_spaces = (width - 2) - (surrounding_spaces * 2)
            result += ' ' * between_spaces
            result += character

        result += ' ' * surrounding_spaces + '\n'

        return result

    @classmethod
    def make_diamond(cls, input_letter):
        if input_letter == 'A':
            return 'A\n'

        a_unicode = ord('A')
        input_unicode = ord(input_letter)

        height = (input_unicode - a_unicode) * 2 + 1
        surrounding_spaces = (height - 1) // 2

        result  = ''

        # Logic for top half and middle row
        for letter_unicode_value in range(a_unicode, (input_unicode + 1)):
            current_character = chr(letter_unicode_value)
            result += cls.make_one_row(height, current_character, surrounding_spaces)

            surrounding_spaces -= 1

        # Reset surrounding spaces
        surrounding_spaces = 1

        # Logic for bottom half
        for letter_unicode_value in range((input_unicode - 1), a_unicode - 1, -1):
            current_character = chr(letter_unicode_value)
            result += cls.make_one_row(height, current_character, surrounding_spaces)

            surrounding_spaces += 1

        return result

if __name__ == '__main__':
    # print(Diamond.make_diamond('A'))
    # print(Diamond.make_diamond('B'))
    print(Diamond.make_diamond('L'))












"""
Main logic:
1. If the letter is A:
    - return just one row 'A\n'
2. Calculate height / width of the diamond = `number of letters between 'A' (inclusive) and the input letter (exclusive) * 2 + 1`
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
"""