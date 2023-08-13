while True:
    try:
        x, y = map(int, input().strip().split(' '))
        perimeter = (x * 2) + (y * 2)
        while y:
            x, y = y, x % y
        print(perimeter // x)
    except EOFError:
        break
    