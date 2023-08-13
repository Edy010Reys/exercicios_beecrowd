while True:
    amount, value_a, value_b = map(int, input().strip().split(' '))
    if amount == value_a == value_b == 0:
        break
    num_a = value_a
    num_b = value_b 
    while num_b:
        num_a, num_b = num_b, num_a % num_b
    mdc = value_a * value_b // num_a
    multiple_mdc = amount // mdc
    multiple_a = amount // value_a
    multiple_b = amount // value_b 
    print(multiple_a + multiple_b - multiple_mdc)
