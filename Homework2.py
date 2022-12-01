# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11
# def sumNums(num):
#     sum = 0
#     for i in str(num):
#         if i != ".":
#             sum += int(i)
#     return sum
#
#
# num = input("Введите число: ")
#
# print(f"{num} -> {sumNums(num)}")

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input("Пусть N = : "))
#
# def mult(n):
#     if n == 1:
#         return 1
#     else:
#         return n * mult(n-1)
#
#
# list = []
# for i in range(1, n + 1):
#     list.append(mult(i))
#
# print(f"тогда произведение чисел от 1 до {n}: {list}")

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#
# Пример:
#
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input("Пусть n = : "))
#
# def mult(n):
#     if n >= 1:
#         return (1+1/n)**n
#
# sum = 0
# list = []
# for i in range(1, n + 1):
#     list.append(round(mult(i),2))
#     sum +=mult(i)
#
# sum = round(sum,2)
# print(f"Для n={n}: {list}")
# print(f"Сумма = {sum}")

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].

# n = int(input("Введите число N: "))
#
# m = -n
# for i in range(m, n+1):
#     print(i, end=' ')

# Реализуйте алгоритм перемешивания списка.
# 
# list = ['Серёжа','Витя','Маша','Паша','Кирилл','Петя']
# 
# list[0],list[1] = list[1], list[0]
# list[2], list[3] = list[3], list[2]
# list[4], list[5] = list[5], list[4]
# 
# print(list)
