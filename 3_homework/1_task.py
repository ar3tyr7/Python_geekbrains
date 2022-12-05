# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

#     - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def Roster (count):
    roaster = []
    for i in range(count):
        roaster.append(int(input(f" Введите {i+1} элемент: ")))
    return roaster
def sum_of_odd (odd):
    sum=0
    for i in range(1,len(odd),2):
        sum+=odd[i]
    return sum

number = int(input("Введите число элементов списка: "))
example = Roster (number)
answer = sum_of_odd(example)
print(answer)
