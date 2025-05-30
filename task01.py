template = "Salom ,mening ismim {first_name} va yoshim {years_old}."

first_name = input("Ismingizni kiriting: ")
years_old = input("Yoshingizni kiriting: ")

result = template.format(first_name=first_name,years_old=years_old)

print(result)