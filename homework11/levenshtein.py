"""Function to calculate Levenshtein distance"""


def calculate_distance(string1, string2):
    """
    :param string1: first string
    :param string2: second string
    :return: Levenshtein distance between a and b
    """
    length1, length2 = len(string1), len(string2)
    if length1 > length2:
        string1, string2 = string2, string1
        length1, length2 = length2, length1

    current_row = range(length1 + 1)
    for i in range(1, length2 + 1):
        previous_row, current_row = current_row, [i] + [0] * length1
        for j in range(1, length1 + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if string1[j - 1] != string2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[length1]


if __name__ == '__main__':
    print(calculate_distance('ewq', 'ewq'))
