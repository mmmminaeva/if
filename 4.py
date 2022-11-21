# Даны три числа. Найти сумму двух наибольших из них.
a, b, c = map(int, input().split())
if a > b > c:
    print(a + b)
if b > c > a:
    print(b + c)
if c > a > b:
    print(c + a)
