class CustomList(list):
    def __init__(self, *args):
        super(CustomList, self).__init__(args)

    def __add__(self, other):
        result = CustomList()
        max_len = max(len(self), len(other))
        for i in range(max_len):
            first_elem = self[i] if i < len(self) else 0
            second_elem = other[i] if i < len(other) else 0
            result.append(first_elem + second_elem)
        return result

    def __sub__(self, other):
        result = CustomList()
        max_len = max(len(self), len(other))
        for i in range(max_len):
            first_elem = self[i] if i < len(self) else 0
            second_elem = other[i] if i < len(other) else 0
            result.append(first_elem - second_elem)
        return result

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
