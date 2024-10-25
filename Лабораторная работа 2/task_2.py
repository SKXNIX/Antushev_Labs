salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
is_increase = False
count_happy_month = 0
money_capital = 0

for i in range(1,months + 1):
    if i > 1:
        spend += spend * increase

    total_spend = salary - spend

    money_capital += int(round(abs(total_spend),0))


print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
