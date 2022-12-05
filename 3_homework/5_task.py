# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
def Fibanachi (count):
    massiv = []
    if count<1: return "Error"
    if count >= 1: 
        massiv.append(1)
        massiv.insert(0,0)
        massiv.insert(0,1)
        i=2
    if count >= 2: 
        massiv.append(1)
        massiv.insert(0,-1)
        i+=2
    while i<2*count:
        massiv.append(massiv[i]+massiv[i-1])  
        massiv.insert(0,massiv[1]-massiv[0])
        i+=2
    return massiv
a=int(input('Введиче число: '))
answer = Fibanachi(a)
print(answer)

