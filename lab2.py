"""
19. Вычислить сумму знакопеременного ряда (-1)^(n-1)*(|х^(2n-2)|)/(2n-2)!,
где х-матрица ранга к (к и матрица задаются случайным образом), n - номер слагаемого.
Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой.
У алгоритма д.б. линейная сложность. Операция умножения –поэлементная.
"""


import numpy as np
from numpy import linalg

print("\nРезультат работы программы:")

matrix_size = int(input('Введите размерность квадратной матрицы больше 1 и меньше 20:'))
while (matrix_size < 1) or (matrix_size > 20):
    matrix_size = int(input("Вы ввели неверное число. " 
    "\nВведите количество строк (столбцов) квадратной матрицы больше 1 и меньше 20:"))

matrix = np.random.randint(-10,11, size=(matrix_size, matrix_size))
det_matrix = np.linalg.matrix_rank(matrix)
print("Матрица:\n", matrix)
print("Ранг матрицы:", det_matrix)

accuracy = int(input('Введите количество знаков после запятой в результате вычисления: '))
accuracy = 0.1**accuracy

n = 1
fact = 1
summa = 0
delta = 0
fraction = 1

while abs(fraction) > accuracy:
    delta += summa
    if n % 2 == 1:
        summa += -1 * ((np.linalg.det(linalg.matrix_power(matrix, 2 * n - 2))) / fact)
    else:
        summa += 1 * ((np.linalg.det(linalg.matrix_power(matrix, 2 * n - 2))) / fact)
    n += 1
    fact = fact * (2 * n + 1) * (2 * n )
    fraction = abs(delta - summa)
    delta = 0
    print(n - 1, ':', summa, ' ', fraction)
print('Сумма знакопеременного ряда:', summa)