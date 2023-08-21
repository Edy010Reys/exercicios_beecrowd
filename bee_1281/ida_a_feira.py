cases = int(input())
while cases > 0:
    cases -= 1
    options = int(input())
    list_options = []
    while options > 0:
        options -= 1
        fruit, price = input().strip().split(' ')
        list_options.append([fruit, float(price)])
    select = int(input())
    list_selected = []
    while select > 0:
        select -= 1
        fruit_selected, amount = input().strip().split(' ')
        list_selected.append([fruit_selected, int(amount)])
    total = 0
    for x in list_options:
        for y in list_selected:
            if x[0] == y[0]:
                total += (x[1] * y[1])
    print('R$ {:.2f}'.format(total))
