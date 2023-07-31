while True:
    numbers = list(map(int, input().split(' ')))
    if sum(numbers) == 0:
        break
    print(sum(numbers))
