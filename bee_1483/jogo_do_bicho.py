from math import ceil

while True:
    v, n, m = input().strip().split(' ')
    if v == n == m == '0':
        break
    if len(n) < 4 or len(m) < 4:
        while len(n) < 4:
            x = list(n)
            x.insert(0, '0')
            n = ''.join(x)
        while len(m) < 4:
            y = list(m)
            y.insert(0, '0')
            m = ''.join(y)
    n = list(n)
    m = list(m)
    number_n = list()
    number_m = list()
    count_one = 0
    while count_one > -4:
        count_one += -1
        num_n = n[count_one]
        num_m = m[count_one]
        number_n.insert(0, num_n)
        number_m.insert(0, num_m)
    n = ''.join(number_n)
    m = ''.join(number_m)
    two_n = list()
    two_m = list()
    count_two = 1
    while count_two < 3:
        count_two += 1
        a = list(n)
        b = list(m)
        two_n.append(a[count_two]) 
        two_m.append(b[count_two])
    two_n = ''.join(two_n)
    two_m = ''.join(two_m)
    number_equal = 0
    count_three = 0
    while count_three > -4:
        count_three += -1
        a = list(n)
        b = list(m)
        var_a = a[count_three]
        var_b = b[count_three]
        if var_a == var_b:
            number_equal += 1
        else:
            break
    if number_equal == 4:
        print('{:.2f}'.format(float(v) * 3000))
    elif number_equal == 3:
        print('{:.2f}'.format(float(v) * 500))
    elif number_equal == 2:
        print('{:.2f}'.format(float(v) * 50))
    elif ceil(int(two_n) / 4) == ceil(int(two_m) / 4):
        print('{:.2f}'.format(float(v) * 16))
    elif number_equal < 2:
        print('{:.2f}'.format(number_equal * 0))