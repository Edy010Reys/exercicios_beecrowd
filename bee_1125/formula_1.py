while True:
    number_bigs_prizes, amount_runners = list(
        map(int, input().strip().split(' '))
    )

    if number_bigs_prizes == amount_runners == 0:
        break

    result_races = [
        list(map(int, input().strip().split(' ')))
        for _ in range(number_bigs_prizes)
    ]

    number_systems_pontuations = int(input())

    list_pontuations = [
        list(map(int, input().strip().split(' ')))
        for _ in range(number_systems_pontuations)
    ]

    for list_numbers in list_pontuations:
        list_numbers.pop(0)

    list_placed = []

    for order in result_races:
        result = [0] * amount_runners
        for pilot, index in enumerate(order, start=1):
            index -= 1
            result.pop(index)
            result.insert(index, pilot)
        list_placed.append(result)
        
    for points in list_pontuations:
        dict_placed = {
            x + 1: 0
            for x in range(amount_runners)
        }

        for order_placing in list_placed:
            for index_point, point in enumerate(points):
                value_new = dict_placed.get(
                    order_placing[index_point]
                ) + point

                dict_placed[order_placing[index_point]] = value_new 

        value_max_dict = max(dict_placed.values())
        
        identifiers = sorted(
            key for key, value in dict_placed.items()
            if value == value_max_dict
        )

        print(*identifiers)
