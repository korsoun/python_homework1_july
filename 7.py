# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

boolean_list = [False, True]
binary_list = [0, 1]
print('Проверка истинности выражения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений X, Y, и Z')

for i in boolean_list:
    x = boolean_list[i]
    printable_x = binary_list[i]
    for j in boolean_list:
        y = boolean_list[j]
        printable_y = binary_list[j]
        for k in boolean_list:
            z = boolean_list[k]
            printable_z = binary_list[k]
            current_boolean = (not(x or y or z)==(not x and not y and not z))
            print(f'Для {printable_x} {printable_y} {printable_z} - {current_boolean}')