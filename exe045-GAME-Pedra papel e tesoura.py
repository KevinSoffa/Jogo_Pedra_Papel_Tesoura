from random import randint
from time import sleep
import emoji
print('''\033[1;36m EU COMPUTADOR TE DESAFIO A JOGAR COMIGO:
VAMOS JOGAR JO KEN PO...\033[m''')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(emoji.emojize('''Suas opções:
[ 0 ]PEDRA :black_circle:
[ 1 ]PAPEL :page_with_curl:
[ 2 ]TESOURA :scissors:'''))
jogador = int(input('Qual é a sua jogada?'))
print('\033[1;31mJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!\033[m')
sleep(1)
print('=-='*12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogagador jogou {}'.format(itens[jogador]))
print('=-='*12)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')

    elif jogador == 1:
        print('EMPATE')

    elif jogador == 2:
        print('JOGADOR VENCE')

    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')

    elif jogador == 1:
        print('COMPUTADOR VENCE')

    elif jogador == 2:
        print('EMPATE')

    else:
        print('JOGADA INVÁLIDA!')