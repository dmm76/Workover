from funcao01 import *

saudar()

saudar_aluno("Douglas")

print(calcula_dobro(10))
print(calcula_dobro_triplo(10))

num = 50
dobro, triplo = calcula_dobro_triplo(num)
print("O dobro de {} é {}".format(num, dobro))
print("O triplo de {} é {}".format(num, triplo))
