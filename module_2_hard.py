# Дополнительное практическое задание по модулю*
# Задание "Слишком древний шифр"

for i in range(3, 21):
    array = []
    array_reverse = []
    array_flag = []

    for j in range(1, i):

        for k in range(1, i):
            if (k != j):
                if (i % (j + k) == 0):
                    array_flag = [j, k]
                    array_reverse = list(reversed(array_flag))
                    if array_reverse in array:
                        continue
                    else:
                        array.append([j, k])
            else:
                continue
    print('Табличка слева |', i, '| - справа', *array)
