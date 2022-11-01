from os import system

import logging as log
from complex_math import get_math_complex_number
from controller import get_output_data, get_input_data
from rational_math import get_math_rational_number


def get_start_calculator():
    log.get_log_data('Старт программы "Калькулятор"')
    new_start = True
    while True:
        if new_start:
            text_start = "Необходимо выбрать с какими числами будете работать: \n1 - Работа с рациональными " \
                         "числами;\n2 - Работа с комплексными числами.\nВвод любого символа кроме 1 и 2 + Enter или " \
                         "Enter закончит программу калькулятора.\n=> "
            working_mode = get_input_data(text_start)
        else:
            text_restart = 'Для продолжения работы нажмите Enter.\nДля выхода из Калькулятора введите любой символ и ' \
                           'нажмите Enter.\n=> '
            working_mode = get_input_data(text_restart)
            if working_mode == '':
                log.get_log_data(
                    'Пользователь выбрал продолжение работы программы "Калькулятор"')
                new_start = True
                system('cls')
                continue
            else:
                text_end = 'Программа "Kалькулятор" закончила работу\n '
                log.get_log_data(text_end)
                get_output_data(text_end)
                break

        if working_mode == '1':  # Работа с рациональными числами
            # Логирование начала работы
            log.get_log_data('Работа с рациональными числами')

            text_rational = 'Введите математическое выражение с рациональными числами в виде -4+2*(3^2/3)\nДля ' \
                            'математических операций используйте операторы  "-", "+","*", "/", "^"(возведение в ' \
                            'степень)\n=> '
            rational_expression = get_input_data(text_rational)  # Введённое выражение
            log.get_log_data(f'Пользователь ввёл=> {rational_expression}')  # Логирование

            bool_error, text_error, rational_number = get_math_rational_number(
                rational_expression)  # решение

            if not bool_error:
                get_output_data(f'{rational_expression} = {rational_number}')
                # Логирование ответ
                log.get_log_data(f'Решение: {rational_expression} = {rational_number}')
            else:
                get_output_data(text_error)
                log.get_log_data('Ошибка. ' + text_error)  # Логирование ошибки
            new_start = False

        elif working_mode == '2':  # Работа с комплексными числами
            log.get_log_data('Работа с комплексными числами')

            text_complex = 'Введите выражения с комплексными числами в виде ' \
                           '((5+3i)+(7-3i))*(2+4i)\nДля математических ' \
                           'операций используйте операторы  "-", "+","*", "/"\n=> '
            complex_expression = get_input_data(text_complex)
            log.get_log_data(f'Пользователь ввёл=> {complex_expression}')

            bool_error, text_error, complex_number = get_math_complex_number(
                complex_expression)

            if not bool_error:
                get_output_data(f'{complex_expression} = {complex_number}')
                log.get_log_data(f'Решение: {complex_expression} = {complex_number}')
            else:
                get_output_data(text_error)
                log.get_log_data('Ошибка. ' + text_error)  # Логирование ошибки
            new_start = False
        else:
            text_end = 'Программа "Kалькулятор" закончила работу\n '
            log.get_log_data(text_end)
            get_output_data(text_end)
            break
