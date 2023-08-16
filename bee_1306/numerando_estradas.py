from math import ceil

number_case = 0
while True:
    number_case += 1
    r, n = map(int, input().strip().split(' '))
    if r == n == 0:
        break
    if n + (n * 26) < r:
        print('Case {}: impossible'.format(number_case))
    else:
        if r - n < 0:
            print('Case {}: 0'.format(number_case))
        else:
            print('Case {}: {}'.format(number_case, ceil((r - n) / n)))