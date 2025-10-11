def rpn1(data: str) -> str:#перевод входной строки в обратную польскую нотацию по алгоритму Дейкстры
    stack_for_operators:list[str] = []
    rpn = ''
    for i in range(len(data)):
        if data[i].isdigit():
            if i > 0 and i <= len(data) - 2:
                if data[i + 1] in '0123456789':
                    rpn += data[i]
                else:
                    rpn += data[i]
                    rpn += ' '
            if i == 0 and len(data) > 1:
                if data[i + 1] in '0123456789':
                    rpn += data[i]
                else:
                    rpn += data[i]
                    rpn += ' '
            if i == 0 and len(data) == 1:
                rpn += data[i]
            if i == len(data) - 1 and len(data) > 1:
                if data[i - 1] in '0123456789':
                    rpn += data[i]
                else:
                    rpn += data[i]
        elif data[i] == '+':
            if i == 0:
                rpn += '+'
            else:
                if stack_for_operators == []:
                    stack_for_operators.append(data[i])
                else:
                    for g in reversed(stack_for_operators):
                        rpn += g
                        rpn += ' '
                    stack_for_operators = []
                    stack_for_operators.append(data[i])
        elif data[i] == '*':
            if len(stack_for_operators) == 0:
                stack_for_operators.append(data[i])
            else:
                if stack_for_operators[-1] == '+' or stack_for_operators[-1] == '-':
                    stack_for_operators.append(data[i])
                else:
                    while (len(stack_for_operators) >= 1) and (stack_for_operators[-1] in '/%*#'):
                        rpn += stack_for_operators[-1]
                        rpn += ' '
                        stack_for_operators.remove(stack_for_operators[-1])
                    stack_for_operators.append('*')
        elif data[i] == '-':
            if i == 0:
                rpn += '-'
            else:
                if stack_for_operators == []:
                    stack_for_operators.append(data[i])
                else:
                    for g in reversed(stack_for_operators):
                        rpn += g
                        rpn += ' '
                    stack_for_operators = []
                    stack_for_operators.append(data[i])
        elif data[i] == '%':
            if len(stack_for_operators) == 0:
                stack_for_operators.append('%')
            else:
                if stack_for_operators[-1] == '+' or stack_for_operators[-1] == '-':
                    stack_for_operators.append(data[i])
                else:
                    while (len(stack_for_operators) >= 1) and (stack_for_operators[-1] in '*/%#'):
                        rpn += stack_for_operators[-1]
                        rpn += ' '
                        stack_for_operators.remove(stack_for_operators[-1])
                    stack_for_operators.append('%')
        elif data[i] == '/':
            if len(stack_for_operators) == 0:
                stack_for_operators.append('/')
            else:
                if stack_for_operators[-1] == '+' or stack_for_operators[-1] == '-':
                    stack_for_operators.append('/')
                else:
                    while (len(stack_for_operators) >= 1) and (stack_for_operators[-1] in '*/%#'):
                        rpn += stack_for_operators[-1]
                        rpn += ' '
                        stack_for_operators.remove(stack_for_operators[-1])
                    stack_for_operators.append('/')
        elif data[i] == '#':
            if len(stack_for_operators) == 0:
                stack_for_operators.append('#')
            else:
                if stack_for_operators[-1] == '+' or stack_for_operators[-1] == '-':
                    stack_for_operators.append('#')
                else:
                    while (len(stack_for_operators) >= 1) and (stack_for_operators[-1] in '*/%#'):
                        rpn += stack_for_operators[-1]
                        rpn += ' '
                        stack_for_operators.remove(stack_for_operators[-1])
                    stack_for_operators.append('#')
        elif data[i] == ' ':
            continue
    if len(stack_for_operators)>=1:
        for r in reversed(stack_for_operators):
            rpn += r
            rpn += ' '
    return rpn

def parse_expression(expr: str) -> list[str]:#Функция преобразует всё в удобный список
    rpn=rpn1(expr)
    stack_for_operators:list[str] = []
    for q in range(len(rpn)):
        if rpn[q] == ' ':
            continue
        elif rpn[q] in '0123456789':
            if rpn[q - 1] in '0123456789-' and q>0:
                stack_for_operators[-1] += rpn[q]
            else:
                stack_for_operators.append(rpn[q])
        else:
            stack_for_operators.append(rpn[q])
    return stack_for_operators