product = [91.79, 1.0, 65, 34.52, 43.7, 13, 52.13, 83.7, 66, 27.08, 75.0, 93, 71.65, 44.4, 44]
for item in product:
    if isinstance(item,float):
        item = str(item)
        ruble, cent = item.split('.')
        if len(cent) != 2:
            cent = f'{cent}0'
        item = f'{ruble} руб {cent} коп'
    else:
        ruble = str(item)
        item = f'{ruble} руб 00 коп'
print(product)
#----------------------------------------------------------------------------------------------
print('\n')

print(product, id(product)) #[91.79, 1.0, 65, 34.52, 43.7, 13, 52.13, 83.7, 66, 27.08, 75.0, 93, 71.65, 44.4, 44] id=3260348882048
product.sort()
print(product, id(product)) #[1.0, 13, 27.08, 34.52, 43.7, 44, 44.4, 52.13, 65, 66, 71.65, 75.0, 83.7, 91.79, 93] id=3260348882048
#----------------------------------------------------------------------------------------------
print('\n')

new_product = product.copy()
new_product.sort(reverse=True)
print(new_product, id(new_product)) #[93, 91.79, 83.7, 75.0, 71.65, 66, 65, 52.13, 44.4, 44, 43.7, 34.52, 27.08, 13, 1.0] id=1930986938816
#----------------------------------------------------------------------------------------------
print('\n')

print(new_product[ :5])
