class Element:
    def __init__(self, datum, next=None):
        self.datum = datum
        self.next = next

    def is_tail(self):
        return self.next is None

class SimpleLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, datum):
        new_head = Element(datum, next=self.head)
        self.head = new_head

    @property
    def size(self):
        count = 0
        current_element = self.head
        while current_element:
            count += 1
            current_element = current_element.next

        return count

    def peek(self):
        return self.head.datum if self.head else None

    def pop(self):
        datum = self.peek()
        self.head = self.head.next
        return datum

    @classmethod
    def from_list(cls, lst):
        linked_list = cls()

        if lst:
            for element in reversed(lst):
                linked_list.push(element)

        return linked_list

    def to_list(self):
        result = []

        current_element = self.head
        while current_element:
            result.append(current_element.datum)
            current_element = current_element.next

        return result

    def reverse(self):
        new_ll = self.__class__()

        current_element = self.head
        while current_element:
            new_ll.push(current_element.datum)
            current_element = current_element.next

        return new_ll


if __name__ == '__main__':
    print(Element(1).datum)