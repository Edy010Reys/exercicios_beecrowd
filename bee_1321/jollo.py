while True:
    list_numbers = list(map(int, input().strip().split(' ')))

    if list_numbers.count(0) == 5:
        break

    for number in range(1, 53):
        if number in list_numbers:
            continue

        numbers_princess = list_numbers[:3]
        numbers_prince = list_numbers[3:]

        numbers_prince.append(number)

        is_bigger = 0

        for number_princess in numbers_princess:
            value_actual = 0

            for number_prince in numbers_prince:
                if number_princess > number_prince:
                    if number_prince > value_actual:
                        value_actual = number_prince         
            
            if not value_actual:
                continue

            if number_princess > value_actual:
                is_bigger += 1
                numbers_prince.remove(value_actual)

        if is_bigger < 2:
            print(number)
            break
    
    else:
        print(-1)