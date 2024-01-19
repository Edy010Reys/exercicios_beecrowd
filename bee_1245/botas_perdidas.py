while True:
    try:
        cases = int(input())
        
        all_shoes = []
        point_found = 0
        while cases > 0:
            shoe = input().strip().upper().split(' ')
            
            size, feet = shoe
            pair_shoe = [size, 'E'] if feet == 'D' else [size, 'D']
            
            if pair_shoe in all_shoes:
                index_shoe_found = all_shoes.index(pair_shoe)
                all_shoes.pop(index_shoe_found)
                point_found += 1

            else:
                all_shoes.append(shoe)

            cases -= 1

        print(point_found)
    except EOFError:
        break