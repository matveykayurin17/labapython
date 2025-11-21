from constants import NUMBERS,OPERATORS
def rpn1(data: str) -> str:
    """
    Перевод входной строки в обратную польскую нотацию по алгоритму Дейкстры
    :param data:строка, введённая пользователем
    :return: строка, переведённая в обратную польскую ноатцию
    """
    stack_for_operators:list[str] = []
    rpn = ''
    for i in range(len(data)):
        if data[i].isdigit():
            if (0 < i <= len(data) - 2) or (i == 0 and len(data) > 1):
                if data[i + 1] in NUMBERS:
                    rpn += data[i]
                else:
                    rpn += data[i]
                    rpn += ' '
            if i == 0 and len(data) == 1:
                rpn += data[i]
            if i == len(data) - 1 and len(data) > 1:
                if data[i - 1] in NUMBERS:
                    rpn += data[i]
                else:
                    rpn += data[i]
        elif data[i] in '+-':
            if i == 0:
                rpn += data[i]
            else:
                if len(stack_for_operators) == 0:
                    stack_for_operators.append(data[i])
                else:
                    for g in reversed(stack_for_operators):
                        rpn += g
                        rpn += ' '
                        stack_for_operators.remove(stack_for_operators[-1])
                    stack_for_operators.append(data[i])
        elif data[i] in OPERATORS:
            if len(stack_for_operators) == 0:
                stack_for_operators.append(data[i])
            else:
                if stack_for_operators[-1] == '+' or stack_for_operators[-1] == '-':
                    stack_for_operators.append(data[i])
                else:
                    while (len(stack_for_operators) >= 1) and (stack_for_operators[-1] in OPERATORS):
                        rpn += stack_for_operators[-1]
                        rpn += ' '
                        stack_for_operators.remove(stack_for_operators[-1])
                    stack_for_operators.append(data[i])
        elif data[i] == ' ':
            continue
    if len(stack_for_operators)>=1:
        for r in reversed(stack_for_operators):
            rpn += r
            rpn += ' '
    return rpn

def parse_expression(expr: str) -> list[str]:
    """
    Функция обращается к функции rpn1
    Строку преобразуем в список
    :param expr: строка, содержащая в себе выражение, переведённое в обратную польскую нотацию
    :return: список, содержащий в себе элементы входной строки без пробелов
    """
    rpn=rpn1(expr)
    stack_for_operators:list[str] = []
    for q in range(len(rpn)):
        if rpn[q] == ' ':
            continue
        elif rpn[q] in NUMBERS:
            if rpn[q - 1] in '0123456789-' and q>0:
                stack_for_operators[-1] += rpn[q]
            else:
                stack_for_operators.append(rpn[q])
        else:
            stack_for_operators.append(rpn[q])
    return stack_for_operators
