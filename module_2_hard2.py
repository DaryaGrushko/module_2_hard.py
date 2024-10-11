# Дополнительное практическое задание по модулю*
# Задание "Слишком древний шифр"
sign = int(input('Введите число от 3 до 20 :'))
str1 = ''
for i in range(1, sign):
    for k in range(i, sign):
       if (k != i):
            if (sign % (k + i) == 0):
                #print(sign,'-' ,i, k)
                str1 = str1 + str(i) + str(k)
print(sign,'-', str1)
