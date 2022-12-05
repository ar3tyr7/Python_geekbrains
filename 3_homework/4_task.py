# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10
def concert_bin (number): 
    massive = []
    while number !=1 or number==0:
        massive.append(number%2)
        number//=2
    massive.append(number)
    massive.reverse()
    return massive
example = 6
answer = concert_bin(example)
print(answer)