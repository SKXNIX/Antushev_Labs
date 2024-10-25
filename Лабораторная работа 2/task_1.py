money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
is_increase = False
count_happy_month = 0
while money_capital > 0:
    if is_increase:
        spend += spend * increase
    else:
        is_increase = True

    total_spend = salary - spend

    if total_spend < 0 < (money_capital + total_spend):
        money_capital += total_spend
    else:
        break

    count_happy_month += 1


print("Количество месяцев, которое можно протянуть без долгов:", count_happy_month)
