while True:
    try:
        letters = input().lower().strip()
        
        vars_ = []
        for i1, l1 in enumerate(letters, start=1):
            if l1 in vars_: 
                continue

            vars_.append(l1)
            result_combs = [
                (let, letters[i1:].index(let) + i1 + 1) 
                for let in set(letters[i1:])
            ]      

            while letters[i1 - 1:] not in vars_:
                combs = []
                for obj_tuple in result_combs:
                    l2, i2 = obj_tuple

                    comb = l1 + l2 if len(l2) < 2 \
                        else [
                            (l2 + l, letters[i2:].index(l) + i2 + 1)
                            for l in set(letters[i2:])
                        ]
                    if isinstance(comb, list):
                        for obj_tuple in comb:
                            l, n = obj_tuple
                            vars_.append(l)

                            if n < len(letters):  
                                combs.append(obj_tuple)

                        continue

                    if i2 < len(letters):
                        combs.append((comb, i2)) 

                    if comb not in vars_: 
                        vars_.append(comb)

                result_combs = combs
        print(*sorted(vars_), sep='\n')
        print()
    except EOFError:
        break
    