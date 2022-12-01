# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
number = int(input("Введите число N: "))
list_n=[]
for i in range(-abs(number),abs(number)+1):
    list_n.append(i)
print(list_n)

s=1
path = 'file.txt'
with open(path, 'r') as data:
    for line in data:
        s*=list_n[int(line)]
    print(s)