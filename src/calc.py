from src.parsing import parse_expression

def calc(expr: str) -> float:#функция вычисляет выражение
    stack_for_operators = parse_expression(expr)
    stack_for_numbers = []
    for i in stack_for_operators:
        if i.isdigit():
            stack_for_numbers.append(i)
        if '-' in i:
            if i == '-':
                op1, op2 = float(stack_for_numbers.pop()), float(stack_for_numbers.pop())
                stack_for_numbers.append(op2 - op1)
            else:
                stack_for_numbers.append(float(i))
        if i in '+*#/%':
            if i == '+':
                op1, op2 = float(stack_for_numbers.pop()), float(stack_for_numbers.pop())
                stack_for_numbers.append(op1 + op2)
            if i == '*':
                op1, op2 = float(stack_for_numbers.pop()), float(stack_for_numbers.pop())
                stack_for_numbers.append(op1 * op2)
            if i == '/':
                op1, op2 = float(stack_for_numbers.pop()), float(stack_for_numbers.pop())
                stack_for_numbers.append(op2 / op1)
            if i == '#':
                op1, op2 = float(stack_for_numbers.pop()), float(stack_for_numbers.pop())
                if str(op1)[-1]=='0' and str(op1)[-2]=='.' and str(op2)[-1]=='0' and str(op2)[-2]=='.':
                    stack_for_numbers.append(int(op2)//int(op1))
                else:
                    raise ValueError('Эта операция выполнима только для целых чисел')
            if i == '%':
                op1, op2 = float(stack_for_numbers.pop()), float(stack_for_numbers.pop())
                if str(op1)[-1]=='0' and str(op1)[-2]=='.' and str(op2)[-1]=='0' and str(op2)[-2]=='.':
                    stack_for_numbers.append(int(op2)%int(op1))
                else:
                    raise ValueError('Эта операция выполнима только для целых чисел')
    return stack_for_numbers[0]