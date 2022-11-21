"""Даны три целых числа, одно из которых отлично от двух других, равных между собой. Определить порядковый номер 
числа, отличного от остальных. """
from operator import index

a = int(input())
b = int(input())
c = int(input())
if a == b:
    print(index(c))
elif c == a:
    print(index(b))
elif c == b:
    print(index(a))
