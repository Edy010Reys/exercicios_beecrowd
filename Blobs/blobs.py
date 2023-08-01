cases = int(input())
while cases > 0:
    amount = float(input())
    days = 0
    cases -= 1
    while amount > 1:
        amount /= 2
        days += 1
    print('{} dias'.format(days))
    