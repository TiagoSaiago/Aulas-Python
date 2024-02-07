import math


def turma(a):
    cont = len(a)
    b = max(a)
    c = sum(a) / len(a)
    if c > 12:
        d = "Boa"
    if 9.5 < c < 12:
        d = "Razoavel"
    else:
        d = "Fraca"
    notas = {"Quantidade de notas": {cont}, "Maior Nota": {b}, "Média da turma:": {c}, "Situação": {d}}
    print(notas)


notas = [12, 15, 8, 5]

turma(notas)
