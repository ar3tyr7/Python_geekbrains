# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

#     - [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19
def sum_of_max_min (massive):
    max = round(massive[0]-int(massive[0]),2)
    min = round(massive[0]-int(massive[0]),2)
    for i in range(1,len(massive)):
        if (round(massive[i]-int(massive[i]),2))>max: max = round(massive[i]-int(massive[i]),2) 
        if (round(massive[i]-int(massive[i]),2))<min: min = round(massive[i]-int(massive[i]),2)
    print(max, min)
    return (max-min)

example = [1.1, 1.2, 3.1, 5.1, 10.01]
answer = sum_of_max_min(example)
print(answer)