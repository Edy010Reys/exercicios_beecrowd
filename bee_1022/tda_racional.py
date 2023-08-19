from fractions import Fraction

cases = int(input())
while cases > 0:
    cases -= 1
    itens = input().strip().split(' ')
    signal = itens[3]
    count = -1
    itens_alt = []
    for var in itens:
        count += 1
        if count == 3:
            itens_alt.append(',')
        if count != 3:
            itens_alt.append(var)
    itens_str = ''.join(itens_alt)
    list_values = itens_str.split(',')
    number = 0
    a = 0
    b = 0
    x = 0
    y = 0
    for value in list_values:
        number += 1
        if number == 1:
            a, b = map(int, value.split('/'))
        else:
            x, y = map(int, value.split('/'))
    if signal == '+':
        n1, n2 = (a * y) + (x * b), (b * y)
        value_red = Fraction(n1, n2)
        if n1 % n2 == 0:
            value_red = '{}/1'.format(value_red)
        print('{}/{} = {}'.format((a * y) + (x * b), (b * y), value_red))
    elif signal == '-':
        n1, n2 = (a * y) - (x * b), (b * y)
        value_red = Fraction(n1, n2)
        if n1 % n2 == 0:
            value_red = '{}/1'.format(value_red)
        print('{}/{} = {}'.format((a * y) - (x * b), (b * y), value_red))
    elif signal == '*':
        n1, n2 = (a * x), (b * y)
        value_red = Fraction(n1, n2)
        if n1 % n2 == 0:
            value_red = '{}/1'.format(value_red)
        print('{}/{} = {}'.format((a * x), (b * y), value_red))
    elif signal == '/':
        n1, n2 = (a * y), (x * b)
        value_red = Fraction(n1, n2)
        if n1 % n2 == 0:
            value_red = '{}/1'.format(value_red)
        print('{}/{} = {}'.format((a * y), (x * b), value_red))
        
          
    