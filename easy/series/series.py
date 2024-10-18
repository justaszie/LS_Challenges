class Series:
    def __init__(self, digits):
        self._digits = digits

    def one_slice(self, start, end):
        return [int(char) for char in self._digits[start:end]]

    def slices(self, series_len):
        string_len = len(self._digits)

        if series_len > string_len:
            raise ValueError(f'Series can have max. length of {string_len}')

        return [self.one_slice(idx, idx + series_len)
                for idx in range(0, (string_len - series_len) + 1)]

if __name__ == '__main__':
    print(Series('02134').slices(1))
    print(Series('002134').slices(2))
    print(Series('02134').slices(3))