from collections import Counter

while True:
    n, m = map(int, input().strip().split(' '))
    if n == m == 0:
        break
    all_values = []
    while n > 0:
        n -= 1
        numbers = list(map(int, input().strip().split(' ')))
        all_values.extend(numbers)
    list_counter = Counter(all_values)
    amount_repeat = []
    for num, amount in list_counter.items():
        if amount not in amount_repeat:
            amount_repeat.append(amount)
    value_second = sorted(amount_repeat)[-2]
    numbers_repeat = []
    for var, repeat in list_counter.items():
        if value_second == repeat and var not in numbers_repeat:
            numbers_repeat.append(var)
    print(' '.join(list(map(str, sorted(numbers_repeat)))) + ' ') 
