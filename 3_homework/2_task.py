# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

#     - [2, 3, 4, 5, 6] => [12, 15, 16];
#     - [2, 3, 5, 6] => [12, 15]
def list_multiply (massive):
    counter = len(massive)//2
    if len(massive) %2 != 0: counter+=1
    answer=[]
    for i in range(counter):
        answer.append(massive[i]*massive[len(massive)-i-1])
    return answer

example = [2, 3, 5, 6]
ans = list_multiply(example)
print(ans)