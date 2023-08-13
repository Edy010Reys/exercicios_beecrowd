cases = int(input())
while cases > 0:
    cases -= 1
    number_1, number_2 = map(int, input().strip().split(' '))
    while number_2:
        number_1, number_2 = number_2, number_1 % number_2
    print(number_1)