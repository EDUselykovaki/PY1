money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
capital=money_capital
month = 0  # количество месяцев, которое можно прожить
while capital>0:
    month=month+1
    capital=capital+salary-spend
    spend=spend*(1+increase)

# TODO Оформить решение

print(month)
