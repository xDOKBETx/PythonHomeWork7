from controller import get_alarm_check
from controller import get_breaking_rational_data

temporary_value = None


def get_math_rational_number(data: str):

    def get_math_operations(list_data):

        global temporary_value

        try:
            if list_data[0] == '-':
                list_data[1] = str(float(list_data[1]) * (-1))
                list_data.pop(0)

            elif list_data[0] == '+':
                list_data.pop(0)
        except (ZeroDivisionError, ValueError, IndexError) as error_signs:
            return get_alarm_check(str(error_signs))

        while True:
            try:
                float(list_data[0])
                if list_data.count('^') > 0:
                    symbol = '^'
                elif list_data.count('*') > 0 or list_data.count('/') > 0:
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

                index_symbol = list_data.index(symbol)
                if symbol == '^':
                    temporary_value = float(
                        list_data[index_symbol - 1]) ** float(list_data[index_symbol + 1])
                elif symbol == '*':
                    temporary_value = float(
                        list_data[index_symbol - 1]) * float(list_data[index_symbol + 1])
                elif symbol == '/':
                    temporary_value = float(
                        list_data[index_symbol - 1]) / float(list_data[index_symbol + 1])
                elif symbol == '+':
                    temporary_value = float(
                        list_data[index_symbol - 1]) + float(list_data[index_symbol + 1])
                elif symbol == '-':
                    temporary_value = float(
                        list_data[index_symbol - 1]) - float(list_data[index_symbol + 1])
                temporary_value = str(temporary_value)
            except (ZeroDivisionError, ValueError, IndexError) as error_signs:
                return get_alarm_check(str(error_signs))

            for _ in range(3):
                list_data.pop(index_symbol - 1)

            list_data.insert(index_symbol - 1, temporary_value)

        number_maths = list_data[0]
        tex_error = ''
        logical_error = False
        return logical_error, tex_error, number_maths

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

                logic_error, snippet_error, temp_number = get_math_operations(
                    new_list_number)
                if logic_error:
                    return logic_error, snippet_error, temp_number

                for _ in range(index_el_2 - index_el_1 + 1):
                    list_number_attributes.pop(index_el_1)

                list_number_attributes.insert(index_el_1, str(temp_number))

                new_list_number.clear()
            except (ZeroDivisionError, ValueError, IndexError) as err:
                return get_alarm_check(str(err))

        logic_error, snippet_error, value_number = get_math_operations(
            list_number_attributes)

        return logic_error, snippet_error, value_number

    list_data_number = get_breaking_rational_data(data)

    bool_error, text_error, number = get_quotes_math(list_data_number)

    return bool_error, text_error, number
