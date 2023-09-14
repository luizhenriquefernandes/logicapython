from datetime import date
'''
1) Data de nascimento: criar um programa que pergunte
ao usuário deu nome e a data de seu nascimento e
calcule a idade com base no ano atual;

2) Crie um programa em que o usuário digite os valores
e o programa calcula a base de um triângulo retângulo.

3) Crie um programa que o usuário digite o peso e a altura
e o programa calcule o IMC índice de massa corporal

4) Crie um programa em que o usuário digite um número em 
graus célsius e o programa converte em farenheit

5) Faça o mesmo para farenheit em Célsius

6) Crie um programa que calcule báskara dos valores digitados
regras a tem que ser sempre elevado ao quadrado x² mas a pode
ter qualquer valor ax² + ou - bx + ou - c = 0
'''

# nome = str(input("Olá qual é o seu nome?\nDigite aqui: "))
# dia = int(input("Digite o dia do seu nascimento: "))
# mes = int(input("Digite o Mês do seu Nascimento: "))
# anoNascimento = int(input('Digite o Ano do seu nascimento: '))
# anoAtual = date.today().year
# idade = anoAtual - anoNascimento
# print(anoAtual)
# print(f'O nome é {nome}')
# print(f'Data de Nascimento: {dia}/{mes}/{anoNascimento} e sua idade é: {idade}')
# print("#"*30)
# print('Cálculo da área de um triângulo retângulo')
# cA = float(input("Digite o Cateto Adjacente: ").replace(",","."))
# cO = float(input("Digite o Cateto Oposto: ").replace(",","."))
# area = (cA*cO)/2
# print(f'A área de um triângulo retângulo é {area:.2f}')

#  x² + x - 8
#  a  +  b -  c

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
delta = float(pow(pow(b,2)-4*a*c,1/2))
print(delta)
x1 = (-b + delta)/2*a
x2 = (-b - delta)/2*a
print(f"x1 = {x1:.2f} e x2 = {x2:.2f}")

teste = pow(1+1,2)
raiz = float(pow(teste,1/2))
print(raiz)

