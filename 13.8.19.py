n = int(input("Введите необходимое количество билетов на онлайн-конференцию\n"))
visitors = dict()
for i in range(1, n+1):
    print("Введите возраст посетителя номер", i)
    age = int(input())
    if age < 18:
        visitors[i] = 0
    elif 18 <= age < 25:
        visitors[i] = 990
    else:
        visitors[i] = 1350
if n > 3:
    print("Вы получаете скидку 10%! Сумма к оплате равна", int(sum(visitors.values()) * 90 / 100), "рублей.")
else:
    print("Сумма к оплате равна", sum(visitors.values()), "рублей.")