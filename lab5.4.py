list = []
num = int(input("Введите целое число (0 для окончания ввода): "))
while num != 0:
    list.append(num)
    num = int(input("Введите целое число (0 для окончания ввода): "))
print(sorted(list, reverse=True),  sep='\r\n')