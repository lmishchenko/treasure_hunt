def execute(number, matrix):
    index = 5 * ((number // 10) - 1) + (number % 10) - 1
    if number == matrix[index]:
        return [number]

    else:
        result = execute(matrix[index], matrix)
        return [number] + result


def test():
    input_data = [55, 14, 25, 52, 21,
                  44, 31, 11, 53, 43,
                  24, 13, 45, 12, 34,
                  42, 22, 43, 32, 41,
                  51, 23, 33, 54, 15]

    expected_result = [11, 55, 15, 21, 44, 32, 13, 25, 43]

    actual_result = execute(11, input_data)
    print(actual_result)
    assert actual_result == expected_result


if __name__ == '__main__':
    test()
