'''
Elaborar um programa que o usuário digite
um número e valide se é par ou ímpar.
data: 12/09/2023   @version 1.0
@autor Prof. Luiz Henrique Fernandes
'''
print('#'*40)
print('Bem vindo ao programa de par ou ímpar')
numero = int(input('Digite o número: '))
if(numero % 2 == 0):
    print(f"\033[34m É par \033[m")
else:
    print(f'\033[31m É ímpar \033[m')
