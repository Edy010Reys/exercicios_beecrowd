while True:
    numbers = list(map(int, input().split(' ')))
    if sum(numbers) == 0:
        break
    numbers_princess = numbers[:3]
    numbers_prince = numbers[3:]
    