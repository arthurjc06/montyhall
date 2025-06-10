from random import randint
vitorias=0
derrotas=0
partidas=0
sair = ''
while True:
    premio = randint(1, 3)
    print('=' * 50)
    print(f'{'PROBLEMA DE MONTY HALL':^50}')
    print('=' * 50)
    if partidas==0:
        print(f'{'Apenas uma porta possui o prêmio':^50}')
    else:
        print(f'''Partidas: {partidas}
Vitórias: {vitorias}
Derrotas: {derrotas}
V/P= {vitorias/partidas}''')
    print('-'*50)
    print(f'{'PORTAS':^50}')
    print(f'{'1          2          3':^50}')
    print('-' * 50)
    porta = portaatual = int(input('Qual porta você escolhe? '))
    while porta <1 or porta>3:
        porta = int(input('Escolha 1, 2 ou 3: '))
    #revelar porta - n pode ser a porta do jogador nem a do premio
    revelar = randint(1,3)
    while revelar==premio or revelar==porta:
        revelar=randint(1,3)
    print('\n'*2)
    mensagem = f'A porta {revelar} foi revelada!'
    print(f'{mensagem:^50}')
    if revelar==1:
        print('-' * 50)
        print(f'{'PORTAS':^50}')
        print(f'{'X          2          3':^50}')
        print('-' * 50)
    elif revelar==2:
        print('-' * 50)
        print(f'{'PORTAS':^50}')
        print(f'{'1          X          3':^50}')
        print('-' * 50)
    elif revelar == 3:
        print('-' * 50)
        print(f'{'PORTAS':^50}')
        print(f'{'1          2          X':^50}')
        print('-' * 50)
    escolha = str(input('\nDeseja trocar de porta? [S/N]: ')).upper()
    while escolha not in 'SN':
        escolha = str(input('Deseja trocar de porta? [S/N]: '))
    if escolha =='S':
        #mudar a porta do jogador
        while portaatual==porta or portaatual==revelar:
            portaatual=randint(1,3)
    print('='*50)
    if portaatual==premio:
        print(f'{'VOCÊ VENCEU!':^50}')
        vitorias+=1
    else:
        print(f'{'VOCÊ PERDEU!':^50}')
        derrotas+=1
    print('=' * 50)
    partidas+=1
    continuar = str(input('\nENTER para CONTINUAR ou qualquer tecla para SAIR: '))
    if continuar!='':
        break
print('='*50)
print(f'{'ESTATÍSTICAS':^50}')
print('='*50)
print(f'''{partidas} PARTIDAS
{vitorias} VITÓRIAS
{derrotas} DERROTAS
PORCENTAGEM DE VITÓRIA: {(vitorias/partidas)*100:.1f}%''')
print('-'*50)
print(f'{'VOLTE SEMPRE!':^50}')
