# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

list_day = [1, 2, 3, 4, 5, 6, 7]
value = int(input('Введите число, соответствующее дню недели: '))
if value > 0 and value < 8:
    for i in list_day:
        if value == list_day[i]:
            day_is_correct = True
            if value == 6 or value == 7:
                print('День выходной')
            else:
                print('День рабочий')
            break
else:
    print('Неправильное число')
