from src.calc import calc

def main():
    data1 = input().replace('//','#')#замена символа // на #
    number=''
    sp=[]
    for k in range(len(data1)-1):#проверка на ошибки
        if data1[k] not in '0123456789*/%#+- ':
            raise ValueError('Неккоректный символ')
    last_c = '1'
    for c in data1:#проверка на два символа идущих подряд
        if  c in '*/-+%#' and last_c in '*/-+%#':
            raise ValueError('два знака не могут идти подряд')
        if c != ' ':
            last_c = c
    print(calc(data1))#вызываем функцию калк
if __name__ == "__main__":
    main()

