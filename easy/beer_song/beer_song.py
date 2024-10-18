
class BeerSong:
    @staticmethod
    def verse(bottle_count):
        bottle_count_str = f"{bottle_count}" if bottle_count > 0 else 'No more'
        bottle_descriptor = 'bottle' if bottle_count == 1 else 'bottles'

        line_1 = f"{bottle_count_str} {bottle_descriptor} of beer on the wall, {bottle_count_str.lower()} {bottle_descriptor} of beer.\n"

        if bottle_count == 0:
            line_2 = "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
        else:
            take_down_descriptor = 'it' if bottle_count == 1 else 'one'
            bottle_descriptor = 'bottle' if (bottle_count - 1) == 1 else 'bottles'
            bottle_count_str = f"{bottle_count - 1}" if (bottle_count - 1) > 0 else 'No more'

            line_2 = f"Take {take_down_descriptor} down and pass it around, {bottle_count_str.lower()} {bottle_descriptor} of beer on the wall.\n"

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