while True:
    list_products = [
        tuple(map(int, input().split(' '))) 
        for _ in range(int(input()))
    ]

    if not list_products:
        break

    list_products.sort(
        key= lambda data: data[0] / data[1],
        reverse=True
    )

    weight_max = int(input())
    price_bigger = 0  
    for index in range(len(list_products)):
        for product in list_products:
            list_loop = [
                product_list
                for product_list in list_products
                if product_list != product
            ]

            list_loop.insert(index, product)

            price_total = 0
            weight_total = 0
            for price, weight in list_loop:          
                weight_total += weight

                if weight_total > weight_max:
                    price_bigger = max(
                        price_bigger, price_total
                    )
                    break
                
                price_total += price
    print(price_bigger)
    