"""
Задание 1.
Написать последовательность Фибоначчи и быть готовым ее модернизировать.


У меня есть базовые знания Python. Поэтому мне удобнее будет писать на нем.
Числа Фибоначчи - последовательность чисел, где каждое последующее число равно сумме двух предыдущих.
Следовательно нам нужен цикл, который будет после сложения двух чисел, присваивать переменной новую сумму, а переменной с меньшим числом - 
присваивать сумму.
Итого на входе мы будем иметь две переменные, каждая из которых равна единице.
Последовательность чисел Фибоначии иногда начинается с 0, иногда с 1. В задании не указано с какого числа она начинается, поэтому я решил 
начать с 1.
Так же в задании не указано что именно должно выводиться на экран:
1) это может быть последовательность чисел, которая будет указана до порядкового номера числа, введенная с клавиатуры
2) это может быть только одно число, порядковый номер которого будет вводиться с клавиатуры.

На языке программирования Python данную задачу можно реализовать несколькими способами.
Я выберу самый простой способ для решения конкретно этой задачи.
"""

x1 = x2 = 1
 
n = int(input())
 
print(x1, x2, end=' ')
 
for i in range(2, n):
    x1, x2 = x2, x1 + x2
    print(x2, end=' ')
