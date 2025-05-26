import add, subtract, mult, divide

while 1:
    action = input('1 - сложение\n2 - вычитание\n3 - умножение\n4 - деление\n>> ')
    a = int(input('число 1: '))
    b = int(input('число 2: '))
    match a:
        case '1':
            r = add(a, b)
            print(f'результат: {r}')
        case '2':
            r = subtract(a, b)
            print(f'результат: {r}')
        case '3':
            r = mult(a, b)
            print(f'результат: {r}')
        case '4':
            r = divide(a, b)
            print(f'результат: {r}')
        case _:
            print('такого варианта нет!')