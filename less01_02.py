str1, str2, strOut = "","",""
print(str1 + ' ' + str2)

for i in range(3):
    str1 = input('Введите дату: ')
    str2 = input('Введите задачу: ')
    strOut += str1 + ' ' + str2 + "\n"
print(strOut)