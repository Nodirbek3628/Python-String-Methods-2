template = "{fruct} maxsuloti narxi ${price}"

fruct = input("Maxsulot nomini kiriting: ")
price = float(input("Narxni kiriting: "))

result = template.format(fruct=fruct,price=price)

print(result)
