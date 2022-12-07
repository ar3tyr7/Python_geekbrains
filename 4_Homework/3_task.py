# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
# Пример:
# - Ввод:[1,1,2,4,5,6,7,7,8], результат: [2,4,5,6,8]


def Filter (massive):
    count=len(massive)
    i=0
    j=0
    flag=False
    while i<count:
        if flag:
            i-=1
            massive.pop(i)
            count-=1
            flag=False
        while j<count:
            if i==j: False
            elif massive[i]==massive[j]: 
                massive.pop(j)
                count-=1
                flag = True
            j+=1
        i+=1
        j=i
    return (massive)
example = [1,1,2,4,5,6,7,7,8,8,8]
a=Filter(example)
print(a)
