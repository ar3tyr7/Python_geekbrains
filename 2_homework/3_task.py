# Задайте словарь из n чисел последовательности (1 + (1/n))^n 
# и выведите на экран их сумму.

#     *Пример:*

#     - Для n = 3:  {1: 2, 2: 2.25 , 3: 2.37}
#     Необходимо сложить все значения словаря и вывести  сумму на экран.
number = int(input("Введите число: "))
ditionary = {}
for i in range(1,number+1):
    ditionary[i]=round((1+(1/i))**i,2)
print(ditionary)