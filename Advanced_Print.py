# Задача 3. Продвинутый print
# start - с чего начинается вывод. По умолчанию пустая строка;
# max_line - максимальная длин строки при выводе. Если строка превышает max_line, то вывод автоматически переносится на новую строку;
# in_file - аргумент, определяющий будет ли записан вывод ещё и в файл.

import builtins

def adv_print(*args, **kwargs):
    list = []
    if 'start' not in kwargs.keys():
        kwargs['start'] = '\n'
    print(kwargs['start'], end='')
    if 'max_line' in kwargs.keys():
        s = str(*args)
        list = [s[x:x+kwargs['max_line']] for x in range (0, len(s), kwargs['max_line'])]
        for element in list:
            print(element)
    if 'in_file' in kwargs.keys():
        if list != []:
            with open(kwargs['in_file'], 'a') as file:
                for element in list:
                    file.write(f'{element} \n')
        else:
            with open(kwargs['in_file'], 'w') as file:
                for element in args:
                    file.write(f'{element} ')
    else:
        builtins.print(*args)


x = 3
y = 2
adv_print(x, y)
adv_print(x, y, start='')
adv_print('Разработать свою реализацию функции print - adv_print', max_line=6, in_file='out.txt')
adv_print(x, y, in_file='output.txt')