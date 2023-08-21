cases = int(input())
while cases > 0:
    cases -= 1
    list_sequences = list(input().strip())
    list_diamonts = []
    for var in list_sequences:
        if var == '<' or var == '>':
            list_diamonts.append(var)
    amount = 0
    count = -1
    for count in range(len(list_diamonts)):
        if count == len(list_diamonts) - 1:
            break
        symbol_before = list_diamonts[count]
        symbol_after = list_diamonts[count + 1]
        if symbol_before == '<' and symbol_after == '>':
            amount += 1
            list_diamonts.pop(count)
            list_diamonts.pop(count)
            list_diamonts.insert(0, symbol_before)
            list_diamonts.insert(1, symbol_after)
    print(amount)
