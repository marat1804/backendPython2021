"""
Custom list class with overloading of arithmetic and logical operators
"""


class CustomList(list):
    """
    Custom List class with +,-,<,<=,==,!=,>,>= operators
    """
    def __init__(self, *args):
        super().__init__(args)

    def __add__(self, other):
        result = CustomList()
        max_len = max(len(self), len(other))
        for i in range(max_len):
            first_elem = self[i] if i < len(self) else 0
            second_elem = other[i] if i < len(other) else 0
            result.append(first_elem + second_elem)
        return result

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        max_len = max(len(self), len(other))
        if len(self) != max_len:
            while len(self) != max_len:
                self.append(0)
        for i in range(max_len):
            second_elem = other[i] if i < len(other) else 0
            self[i] = self[i] + second_elem
        return self

    def __sub__(self, other):
        result = CustomList()
        max_len = max(len(self), len(other))
        for i in range(max_len):
            first_elem = self[i] if i < len(self) else 0
            second_elem = other[i] if i < len(other) else 0
            result.append(first_elem - second_elem)
        return result

    def __rsub__(self, other):
        return self.__sub__(other)

    def __isub__(self, other):
        max_len = max(len(self), len(other))
        if len(self) != max_len:
            while len(self) != max_len:
                self.append(0)
        for i in range(max_len):
            second_elem = other[i] if i < len(other) else 0
            self[i] = self[i] - second_elem
        return self

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)
