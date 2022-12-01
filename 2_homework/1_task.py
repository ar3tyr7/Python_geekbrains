# Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.(Сделать для строки)

#     *Пример:*

#     - 6782 -> 23
#     - 0,56 -> 11
number = str(input("Введите число: "))
number = number.replace(",","")
# result = list(number)
result = [int(i) for i in list(number)]
print(sum(result))