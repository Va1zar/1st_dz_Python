# Задача 2: Найдите сумму цифр трехзначного числа.

a = int(input())
print(a//100 + a%100//10 + a%10)