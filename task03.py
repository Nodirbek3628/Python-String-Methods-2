template = "Fayl:{document}.{doc_type}"

document = input("Hisobotingzni kirirting: ")
doc_type = input("hujjat turini kiriritng: ")

result = template.format(document=document,doc_type=doc_type)

print(result)