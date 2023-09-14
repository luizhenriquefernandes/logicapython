from datetime import date

dia = int(date.today().day)
mes = int(date.today().month) * 30
ano = int(date.today().year) * 360

dianasc = int(input('Digite seu dia de nascimento:'))
mesnasc = int(input('Digite seu mes de nascimento:')) * 30
anonasc = int(input('Digite seu ano de nascimento:')) * 360

atual = dia + mes + ano
nasc = dianasc + mesnasc + anonasc

print(f'voce tem {(atual-nasc)//360} anos {((atual-nasc)%360)//30}')

