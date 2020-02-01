class Input:
    def __init__(self, matrix):
        self.data = matrix

    def number_by_index(self, row, column):
        return self.data[row][column]


class Output:
    def __init__(self):
        self.result = []

    def __repr__(self):
        return " ".join(map(lambda x: str(x), self.result))

    def extend(self, new_number):
        self.result.append(new_number)


class TreasureHunt:
    def __init__(self, input):
        self.input = input

    def execute(self):
        number = 11

        next_number = self.next_number(number)
        output = Output()

        while number != next_number:
            output.extend(number)
            number = next_number
            next_number = self.next_number(number)

        output.extend(number)

        return output

    def next_number(self, number):
        row = number // 10 - 1
        column = number % 10 - 1
        next_number = self.input.number_by_index(row, column)

        return next_number


class Test:
    input_data = [[55, 14, 25, 52, 21],
                  [44, 31, 11, 53, 43],
                  [24, 13, 45, 12, 34],
                  [42, 22, 43, 32, 41],
                  [51, 23, 33, 54, 15]]

    expected_result = [11, 55, 15, 21, 44, 32, 13, 25, 43]
    full_input = Input(matrix=input_data)
    actual_result = TreasureHunt(full_input).execute()

    assert actual_result.result == expected_result
