def ShopOLAP(N, items):
    result = SortSalesDesc(GroupSalesByProducts(items))
    return result


def SortLexicographically(product1, product2):
    if product1 < product2:
        return product1, product2
    else:
        return product2, product1


def SortSalesDesc(input):
    products = input[0]
    counts = input[1]
    for i in range(len(products) - 1):
        for j in range(i + 1, len(products)):
            if counts[j] > counts[i]:
                counts[i], counts[j] = counts[j], counts[i]
                products[i], products[j] = products[j], products[i]
            elif counts[j] == counts[i]:
                products[i], products[j] = SortLexicographically(products[i], products[j])
    input = [f"{products[i]} {counts[i]}" for i in range(len(products))]
    return input


def GroupSalesByProducts(items):
    products = []
    counts = []
    for i in items:
        if i.split()[0] in products:
            counts[products.index(i.split()[0])] += int(i.split()[1])
        else:
            products.append(i.split()[0])
            counts.append(int(i.split()[1]))
    return [products, counts]
