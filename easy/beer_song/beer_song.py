
class BeerSong:
    @staticmethod
    def verse(verse_number):
        if verse_number == 0:
            line_1 = "No more bottles of beer on the wall, no more bottles of beer.\n"
            line_2 = "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
        else:
            if verse_number == 1:
                line_1 = "1 bottle of beer on the wall, 1 bottle of beer.\n"
                line_2 = "Take it down and pass it around, no more bottles of beer on the wall.\n"

            else:
                line_1 = f"{verse_number} bottles of beer on the wall, {verse_number} bottles of beer.\n"

                if verse_number == 2:
                    line_2 = f"Take one down and pass it around, 1 bottle of beer on the wall.\n"
                else:
                    line_2 = f"Take one down and pass it around, {verse_number - 1} bottles of beer on the wall.\n"

        return line_1 + line_2

    @classmethod
    def verses(cls, number_from, number_to):
        verses_list = [ cls.verse(verse_number)
                       for verse_number
                       in range (number_from, number_to - 1, -1)
                    ]

        return '\n'.join(verses_list)

    @classmethod
    def lyrics(cls):
        return cls.verses(99, 0)


if __name__ == '__main__':
    # print(BeerSong.verses(0)) # (0, 0)
    # print(BeerSong.verses()) # (99, 0)
    print(BeerSong.verses(2, 0)) # (99, 90)