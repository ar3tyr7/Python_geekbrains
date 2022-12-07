# Вычислить число Пи c заданной точностью d

# Пример:

#     - при d = 0.0001,  π = 3.1415    10^-1 ≤ d ≤10^-10
import math
def pi(accuracy):
    count=0
    while accuracy<=1:
        accuracy*=10
        count+=1
    return (round((math.pi),count-1))
number=float(input("Введиет необходимую точность: "))
answer = pi(number)
print(answer)