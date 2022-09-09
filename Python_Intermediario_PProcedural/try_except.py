# # a = []
# try:
#     a = 1/0
# except:
#     print('erro')

# print(a)

# print

from decimal import DivisionByZero


try:
    print(a)
except NameError as erro:
    print(erro)


def divide(n1, n2):
    if n2 == 0:
        raise DivisionByZero('n2 não pode ser zero!!')  # Levanatando as proprias excessões
    return n1 / n2


print(divide(3, 0))
