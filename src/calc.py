from src.constants import NUMBERS_AND_OPERATORS,FULL_OPERATORS
from src.parsing import parse_expression
import operator
def calc(expr: str) -> float|int:
    """
    Функция вычисляет выражение
    :param expr: принимает входную строку
    :return: значение арифмитического выражения
    """
    expr=expr.replace('//','#')
    for k in range(len(expr) - 1):  # проверка на ошибки
        if expr[k] not in NUMBERS_AND_OPERATORS:
            raise ValueError('Неккоректный символ')
    last_c = '1'
    for c in expr:  # проверка на два символа идущих подряд
        if c in FULL_OPERATORS and last_c in FULL_OPERATORS:
            raise ValueError('два знака не могут идти подряд')
        if c != ' ':
            last_c = c
    if expr=='':
        raise ValueError('пустую строку нельзя поддавать на ввод')
    operators1={'+':operator.add,'/':operator.truediv,'*':operator.mul}
    stack_for_operators = parse_expression(expr)
    stack_for_numbers:list[float|int] = []
    for i in stack_for_operators:
        if i.isdigit():
            stack_for_numbers.append(float(i))
        if '-' in i:
            if i == '-':
                op1, op2 = float(stack_for_numbers.pop()), float(stack_for_numbers.pop())
                stack_for_numbers.append(op2 - op1)
            else:
                stack_for_numbers.append(float(i))
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
        if i in '+/*':
            op1,op2=float(stack_for_numbers.pop()),float(stack_for_numbers.pop())
            now=operators1[i](op2,op1)
            stack_for_numbers.append(now)
    return stack_for_numbers[0]
