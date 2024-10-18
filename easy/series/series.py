class Series:
    def __init__(self, digits):
        self._digits = digits

    def one_slice(self, start, end):
        slice = self._digits[start:end]
        return [int(char) for char in slice]

    def slices(self, series_len):
        string_len = len(self._digits)

        if series_len > string_len:
            raise ValueError(f'Series can have max. length of {string_len}')

        result = []
        for idx in range(0, (string_len - series_len) + 1):
            slice = self.one_slice(idx, idx + series_len) # 5digits, length 2. Goes up to indexes 3-5(excl)
            result.append(slice)

        return result

if __name__ == '__main__':
    print(Series('02134').slices(1))
    print(Series('002134').slices(2))
    print(Series('02134').slices(3))