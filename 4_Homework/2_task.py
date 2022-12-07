# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
import math
def Multipliers(number):
    divider = 2
    multipliers=[]
    tmp=number
    while divider<=abs(tmp):
        if tmp%divider == 0: 
            multipliers.append(divider)
            tmp=tmp/divider
            if tmp == divider and math.prod(multipliers)==number: break
            divider=1
        divider+=1
    print(multipliers)
exampel = int(input("Введите число: "))
Multipliers(exampel)