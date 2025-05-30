template = "Bugun {week_day} kuni, dars soat {hour}:00 da."

week_day = input("kunni kiriting: ")
hour = int(input("dars soatini kiriting: "))

result = template.format(week_day=week_day,hour=hour)

print(result)