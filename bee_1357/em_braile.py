while True:
    braile_dict = {
        '1' : '*.\n..\n..',
        '2' : '*.\n*.\n..',
        '3' : '**\n..\n..',
        '4' : '**\n.*\n..',
        '5' : '*.\n.*\n..',
        '6' : '**\n*.\n..',
        '7' : '**\n**\n..',
        '8' : '*.\n**\n..',
        '9' : '.*\n*.\n..',
        '0' : '.*\n**\n..',
    }
    number = int(input())
    if number == 0:
        break

    letter = input().strip().upper()
    if letter == 'S':
        sequence = input().strip()
        index_zero = []
        index_one = []
        index_two = []
        for var in sequence:
            value = braile_dict[var].split('\n')
            index_zero.append(value[0])
            index_one.append(value[1])
            index_two.append(value[2])
        print(' '.join(index_zero))
        print(' '.join(index_one))
        print(' '.join(index_two))

    elif letter == 'B':
        list_geral = []
        count = 0
        lines = 3
        while lines > 0:
            lines -= 1 
            sequence_braile = input().strip().split(' ')
            count = len(sequence_braile)
            list_geral.append(sequence_braile)
        
        list_numbers = []
        for x in range(count):
            list_z = []
            for y in range(len(list_geral)):
                if y < 3 or (y >= 3 and x < 3):
                    list_z.append(list_geral[y][x])
            braile = '\n'.join(list_z)
            for num in range(10):
                num = str(num)
                value_braile = braile_dict[num]
                if braile == value_braile:
                    list_numbers.append(num)
        print(''.join(list_numbers))
        