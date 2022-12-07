# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100)* многочлена и записать в файл многочлен степени k.

#     *Пример:* 

#     - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#     -  k=5 => 2*x^5 + 4*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0
import random
def Function (k):
    answer = str()
    for i in range(k+1):
        koef = random.randint(0,100)
        if (k-i)==k:
            answer += f'{random.randint(1,100)}*x^{k-i} + '
        elif koef!=0:
            if i==k:
                answer+=f'{koef} + '
            else: 
                answer += f"{koef}*x^{k-i} + "
    answer =answer[0:-2] + '= 0'   
    return answer 
  
example = Function(9)
print (example)
