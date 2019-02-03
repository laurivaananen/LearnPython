products = [('milk', 5.5), ('candy', 2.5), ('bread', 9.0)]

def product_sorter(product):
    name, price = product
    return len(name)

sorted_by_name_length = sorted(products, reverse=True, key=product_sorter)
sorted_by_price = sorted(products, reverse=True, key=lambda x: x[1])

print(products)
print(sorted_by_name_length)
print(sorted_by_price)