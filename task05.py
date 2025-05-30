template = "{num01} + {num02} = {sum}"

num01 = int(input("raqamni kiriting: "))
num02 = int(input("raqamni kiriting: "))
sum = num01 + num02
result = template.format(num01=num01,num02=num02,sum=sum)

print(result)