while True:
    try:
        total_points = 0
        t, n = map(int, input().strip().split(' '))
        if t == n == 0:
            break
        while t > 0:
            t -= 1
            country, points = input().strip().split(' ')
            points = int(points)
            total_points += points
        total_possible = n * 3
        print(total_possible % total_points)
    except ZeroDivisionError:
        print(0)
        