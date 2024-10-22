class CustomSet:
    def __init__(self, lst=[]):
        self._members = []

        for element in lst:
            self.add(element)

    @property
    def members(self):
        return self._members

    def is_empty(self):
        return len(self.members) == 0

    def contains(self, number):
        return number in self.members

    def add(self, number):
        if number not in self.members:
            self.members.append(number)

    def is_same(self, other_set):
        return len(self.members) == len(other_set.members) and self.is_subset(other_set)

    def __eq__(self, other):
        if not isinstance(other, CustomSet):
            return NotImplemented

        return self.is_same(other)

    def is_subset(self, other_set):
        # returns true even if self.members is empty
        # TODO - use contains instead of accessing members directly
        return all([other_set.contains(member) for member in self._members])

    def intersection(self, other_set):
        result = [member for member in self.members if other_set.contains(member)]
        return CustomSet(result)

    def is_disjoint(self, other_set):
        return self.intersection(other_set).is_empty()

    def difference(self, other_set):
        result = [member for member in self.members if not other_set.contains(member)]
        return CustomSet(result)


    def union(self, other_set):
        result = CustomSet(self.members)

        for member in other_set.members:
            result.add(member)

        return result
