import random

class Robot:
    _taken_names = set()

    def __init__(self):
        self.set_new_name()

    def reset(self):
        self.__class__._taken_names.remove(self.name)
        self.set_new_name()

    @property
    def name(self):
        return self._name

    def set_new_name(self):
        self._name = None


        while True:
            new_name = self.__class__.generate_name()
            if new_name not in self.__class__._taken_names:
                break

        self._name = new_name
        self.__class__._taken_names.add(self.name)

    @classmethod
    def generate_name(cls):
        letters = [chr(unicode_value) for unicode_value in range(ord('A'), ord('Z') + 1)]
        digits = [str(digit) for digit in range (10)]

        result = ''
        result += ''.join(random.choices(letters, k=2))
        result += ''.join(random.choices(digits, k=3))

        return result


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