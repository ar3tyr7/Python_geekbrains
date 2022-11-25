# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

arrayBool = [False,True]
for x in arrayBool:
    for y in arrayBool:
        for z in arrayBool:
            print((not (x or y or z)) == ((not x) and (not y) and (not z)))
