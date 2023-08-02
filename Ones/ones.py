while True:
    try:
        number = int(input())
        if number % 2 == 0 or number % 5 == 0:
            continue
        value_dynamic = 1
        decimal_place = 1
        point = 1
        while True:
            if value_dynamic % number != 0:
                decimal_place *= 10
                value_dynamic += decimal_place
                point += 1
            else:
                print(point)
                break
    except EOFError:
        break
