"""Дано целое число. Если оно является положительным, то вычесть из него 8; если отрицательным, то прибавить к нему 6;
если нулевым, то заменить его на 10. Вывести полученное число."""
n = int(input())
c = n - 8
if n > 0:
    print(c)
if n < 0:
    print(c + 6)
if n == 0:
    print(10)
