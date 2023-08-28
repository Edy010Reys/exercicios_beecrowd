while True:
    try:
        number = int(input())
        start = list(map(int, input().strip().split(' ')))
        ended = list(map(int, input().strip().split(' ')))
        count = -1
        total = 0
        for num in ended:
            count += 1
            index_start = start.index(num)
            index_ended = ended.index(num)
            diff = abs(index_ended - index_start)
            total += diff
            start.pop(index_start)
            start.insert(count, num)
        print(total)
    except EOFError:
        break
