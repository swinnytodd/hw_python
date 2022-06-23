def check_sym(test_str, position, str_length):
    if position == str_length:
        print(int(test_str) // 2 if int(test_str) % 2 == 0 else int(test_str) * 3 + 1)
        return
    if '0' <= test_str[position] <= '9':
        position += 1
        check_sym(test_str, position, str_length)
    else:
        if test_str == 'cancel':
            print('Bye!')
            return
        print('не получилось преобразовать.')


input_list = input()
check_sym(input_list, 0, len(input_list))