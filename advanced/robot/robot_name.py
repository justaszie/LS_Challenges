import random

class Robot:
    taken_names = set()

    def __init__(self):
        new_name = self.__class__.generate_name()
        while new_name in self.__class__.taken_names:
            new_name = self.__class__.generate_name()

        self.name = new_name

        # self.__class__.taken_names.add(new_name)

    # TODO: review repetition of name generation lines
    def reset(self):
        self.__class__.taken_names.remove(self.name)

        new_name = self.__class__.generate_name()
        while new_name in self.__class__.taken_names:
            new_name = self.__class__.generate_name()

        self.name = new_name

        # self.__class__.taken_names.add(new_name)

    @classmethod
    def generate_name(cls):
        result = ''

        letters = [chr(unicode_value) for unicode_value in range(ord('A'), ord('Z') + 1)]
        digits = [str(digit) for digit in range (10)]

        for _ in range(2):
            result += random.choice(letters)

        for _ in range(3):
            result += random.choice(digits)

        return result

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name
        self.__class__.taken_names.add(self.name)

if __name__ == '__main__':
    robot1 = Robot()
    robot2 = Robot()

    print(robot1.name)
    print(robot2.name)

    robot1.reset()
    robot2.reset()

    print('NEW')

    print(robot1.name)
    print(robot2.name)

    print(f"Taken names: {Robot.taken_names}")