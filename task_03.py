# Запрашиваем пользователя:
month = int(input("Введите номер месяца: "))
# На экране отображен введенный месяц:
print('Вы ввели', month)
# На консоль выведено кол-во дней этого месяца (без указания названия месяца, в феврале 28 дней)
months_31 = [1, 3, 5, 7, 8, 10, 12]
months_30 = [4, 6, 9, 11]
months_28 = [2]
if month in months_31:
  print('31')
elif month in months_30:
  print('30')
elif month in months_28:
  print('28') 
# Выведено сообщение, если номер месяца некорректен
else: print('Ввод месяца осуществлен некорректно')
  
# Отлично. Можно еще так
# Решение 2
import calendar as cl  # используем модуль для получения функции

year_input = input("Введите год: ")
month_input = input("Введите номер месяца: ")

year = int(year_input)
month_ = int(month_input)
print(cl.monthrange(year, month_))
