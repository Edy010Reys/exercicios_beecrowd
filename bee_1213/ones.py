while True:
    try:
        number = int(input())
        value = 1
        point = 1
        while value % number != 0:
            value = (value * 10) + 1 % number
            point += 1
        print(point)
    except EOFError:
        break
