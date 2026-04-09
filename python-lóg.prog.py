'''Primeira Questão'''
N = int(input("Digite um número: "))
Qtde = 0
M = 0
while Qtde <= 10:
    M = N * Qtde
    print(M)
    Qtde = Qtde + 1

    
"""Do while"""

'''Segunda Questão'''
Mi = int(input("Digite um valor mínimo:"))
Ma = int(input("Digite um valor máximo: "))
if Mi > Ma:
    print("Valores inválidos")
else:
    while Mi <= Ma:
        if Mi % 5 == 0:
            print(Mi)
        Mi = Mi + 1

