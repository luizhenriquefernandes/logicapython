from datetime import date
'''Condicionais é importante para se fazer comparações entre vairáveis ou
valores boolenos, numéricos eu de palavras
Para realizar esses elementos é importante utilizar a condição if seiguida de
um senão else ou nada
'''
diaAtual = date.today().day
mesAtual = date.today().month
anoAtual = date.today().year
diaNascimento = int(input('Dia do Nascimento: '))
mesNascimento = int(input('Mês do Nascimento: '))
anoNascimento = int(input('Ano do Nascimento: '))
print(f'{diaAtual}/{mesAtual}/{anoAtual}')
if(mesNascimento == mesAtual):
    print('Estou no mes de aniversário')
    if(diaNascimento == diaAtual):
        print('Hoje é dia do meu aniversário')
        idade = anoAtual - anoNascimento
        print(f'Minha idade é {idade} anos de vida')
    elif(diaNascimento < diaAtual):
        print('Já fiz aniversário')
        idade = anoAtual - anoNascimento
        print(f'Minha idade é {idade} anos de vida')
    else:
        print('Ainda não fiz aniversário mas estou no mes')
        idade = (anoAtual - anoNascimento)-1
        print(f'Minha idade é {idade} anos de vida')
elif(mesNascimento < mesAtual):
    print('O mes de nascimento é menor que o mes atual')
    print('Já fiz aniversário 😎')
    idade = anoAtual - anoNascimento
    print(f'Minha idade é {idade} anos de vida')  
else:
    print('O mes de nascimento é maior que o mes atual')
    print('Não fiz aniversário 😡')
    idade = (anoAtual - anoNascimento)-1
    print(f'Minha idade é {idade} anos de vida')
