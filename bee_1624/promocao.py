while True:
    cases = int(input())
    if cases == 0:
        break
    products = []
    for var in range(cases):
        price, weight = map(int, input().split(' '))
        products.append((price, weight))
    max_weight = int(input())
    dp = [0] * (max_weight + 1)
    for price, weight in products:
        for w in range(max_weight, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + price)
    print(dp[max_weight])
