# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

number = input("Введите трёхзначное число = ")
a = int(number[0])
b = int(number[1])
c = int(number[2])
result = a + b + c
print(result)