from math import sqrt

while True:
    try:
        d, vf, vg = map(int, input().strip().split(' '))
        move_g = sqrt((12 ** 2) + (d ** 2))
        time_f = 12 / vf
        time_g = move_g / vg
        if time_g <= time_f:
            print('S')
        else:
            print('N')
    except EOFError:
        break
