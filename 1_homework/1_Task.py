# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#  и проверяет, является ли этот день выходным.
# Пример:
#                 - 6 -> да
#                 - 7 -> да
#                 - 1 -> нет
a = int(input(f'Введите день недели от 1 до 7: '))
if a > 0 and a < 6:
    print('нет')
elif a > 5 and a<8:
    print('да')
else:
    print('Введены некорректные данные')


 # Final project
# text= 'A/5 21171'
# def lucky (ticket):
#     i=0
#     while i< len(ticket):
#         if ticket[i] == " ":
#             ticket = ticket[i+1:]
#         i+=1
#     return ticket

# answer = lucky(text)
# print(answer)
