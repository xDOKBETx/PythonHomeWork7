def get_input_data(data):
    return input(data)


def get_output_data(data):
    print(data)


def get_alarm_check(error_output: str):
    if error_output == 'float division by zero':
        return True, 'При решении выражения появилось деление на 0', None
    elif error_output.find('could not convert string to float:') > -1:
        return True, 'Выражение введено неправильно,посмотрите пример выше', None
    elif error_output.find('no signs') > -1:
        return True, 'Выражение введено неправильно.Не хватает оператора математических выражений', None
    elif error_output.find('list index out of range') > -1:
        return True, 'Выражение введено неправильно.', None
    elif error_output == 'no i':
        return True, 'Выражение введено неправильно.В комплексном выражении не хватает i.', None
    elif error_output == 'no ()':
        return True, 'Выражение введено неправильно.В комплексном выражении не хватает круглых скобок.', None
    else:
        return True, 'Выражение введено неправильно.', None


def get_breaking_rational_data(math: str):
    math = math.replace(' ', '')

    symbol = ['^', '*', '/', '+', '-', '(', ')']

    for signs in symbol:
        math = math.replace(signs, f'#{signs}#')

    list_number_math = math.split('#')
    list_data = [data for data in list_number_math if data != '']

    return list_data


# noinspection PyTypeChecker
def get_breaking_complex_data(math: str):
    math = math.replace(' ', '')

    math = math.replace('(', '#(')
    math = math.replace(')', ')#')

    list_number_math = math.split('#')
    list_data = [data for data in list_number_math if data != '']

    for index, data in enumerate(list_data):
        if data != '*' and data != '/' and data != '+' and data != '-' and data != '(' and data != ')':
            if data.find('i') == -1:
                its_error = 'no i'
                return get_alarm_check(its_error)
            if data.find('(') == -1 or data.find(')') == -1:
                its_error = 'no ()'
                return get_alarm_check(its_error)
            data = data.replace('(', '')
            data = data.replace(')', '')
            data = data.replace('i', '')
            data = data.replace('-', '#-')
            data = data.replace('+', '#+')
            list_data[index] = data.split('#')

    return False, '', list_data
