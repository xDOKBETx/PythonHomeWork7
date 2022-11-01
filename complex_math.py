from controller import get_alarm_check
from controller import get_breaking_complex_data

temporary_value_one = None
temporary_value_two = None


def get_math_complex_number(data: str):
    def get_math_operations(list_data: list):

        global temporary_value_one, temporary_value_two

        while True:
            try:
                float(list_data[0][0])
                float(list_data[0][1])
                if len(list_data) > 1 and list_data.count('*') == 0 and list_data.count('/') == 0 and list_data.count(
                        '+') == 0 and list_data.count('-') == 0:
                    error_signs = 'no signs'
                    return get_alarm_check(str(error_signs))

                if list_data.count('*') > 0 or list_data.count('/') > 0:
                    if list_data.count('*') > 0 and list_data.count('/') > 0 and (
                            list_data.index('*') < list_data.index('/')):
                        symbol = '*'
                    elif list_data.count('*') > 0 and list_data.count('/') > 0 and (
                            list_data.index('/') < list_data.index('+')):
                        symbol = '/'
                    elif list_data.count('*') > 0:
                        symbol = '*'
                    else:
                        symbol = '/'
                elif list_data.count('+') > 0 or list_data.count('-') > 0:
                    if list_data.count('+') > 0 and list_data.count('-') > 0 and (
                            list_data.index('+') < list_data.index('-')):
                        symbol = '+'
                    elif list_data.count('-') > 0 and list_data.count('+') > 0 and (
                            list_data.index('-') < list_data.index('+')):
                        symbol = '-'
                    elif list_data.count('+') > 0:
                        symbol = '+'
                    else:
                        symbol = '-'
                else:
                    break

                index_attribute = list_data.index(symbol)
                a = float(list_data[index_attribute - 1][0])
                b = float(list_data[index_attribute - 1][1])
                c = float(list_data[index_attribute + 1][0])
                d = float(list_data[index_attribute + 1][1])
                if symbol == '*':
                    temporary_value_one = a * c - b * d
                    temporary_value_two = b * c + a * d
                elif symbol == '/':
                    temporary_value_one = (a * c - b * d) / (c ** 2 + d ** 2)
                    temporary_value_two = (b * c - a * d) / (c ** 2 + d ** 2)
                elif symbol == '+':
                    temporary_value_one = a + c
                    temporary_value_two = b + d
                elif symbol == '-':
                    temporary_value_one = a - c
                    temporary_value_two = b - d
                temp_number = [str(temporary_value_one),
                               str(temporary_value_two)]
            except (ZeroDivisionError, ValueError, IndexError) as error_signs:
                return get_alarm_check(str(error_signs))

            for _ in range(3):
                list_data.pop(index_attribute - 1)

            list_data.insert(index_attribute - 1, temp_number)

        return False, '', list_data[0]

    def get_quotes_math(list_number_attributes: list):

        while list_number_attributes.count('(') > 0:
            try:
                index_el_1 = -1
                index_el_2 = -1

                for i, x in enumerate(list_number_attributes):
                    if x == '(':
                        index_el_1 = i
                    if x == ')' and index_el_1 != -1:
                        index_el_2 = i
                        break

                new_list_number = [list_number_attributes[ind]
                                   for ind in range(index_el_1 + 1, index_el_2)]

                logical_error, snippet_error, temp_number = get_math_operations(
                    new_list_number)
                if logical_error:
                    return logical_error, snippet_error, temp_number

                for _ in range(index_el_2 - index_el_1 + 1):
                    list_number_attributes.pop(index_el_1)

                list_number_attributes.insert(index_el_1, temp_number)

                new_list_number.clear()
            except (ZeroDivisionError, ValueError, IndexError) as err:
                return get_alarm_check(str(err))

        return get_math_operations(list_number_attributes)

    bool_error, text_error, list_data_number = get_breaking_complex_data(data)

    if not bool_error:
        bool_error, text_error, using_number = get_quotes_math(list_data_number)

    if not bool_error:

        # noinspection PyUnboundLocalVariable
        if float(using_number[0]) != 0 and float(using_number[1]) > 0:
            complex_str = f'({using_number[0]}+{str(float(using_number[1]))}i)'
        elif float(using_number[0]) != 0 and float(using_number[1]) < 0:
            complex_str = f'({using_number[0]}{using_number[1]}i)'
        elif float(using_number[0]) == 0:
            complex_str = f'{using_number[1]}i'
        else:
            complex_str = '0'
    else:
        complex_str = None

    return bool_error, text_error, complex_str
