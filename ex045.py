from random import randint
print('{:#^40}'.format(' JOGO PEDRA PAPEL TESOURA '))
print('''[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
opcao = int(input('Qual a sua jodada? '))
comp = randint(1, 3)
print(comp)
if opcao == 1: #pedra
    if comp == 1:
        print('Deu EMPATE! Nós dois escolhemos PEDRA!')
    elif comp == 2:
        print('Eu VENCI!! Eu escolhi PAPEL e você PEDRA')
    else:
        print('Você VENCEU!!! Eu escolhi TESOURA e você PEDRA')
elif opcao == 2: #papel
    if comp == 2:
        print('Deu EMPATE! Nós dois escolhemos PAPEL!')
    elif comp == 3:
        print('Eu VENCI!! Eu escolhi TESOURA e você PAPEL')
    else:
        print('Você VENCEU!!! Eu escolhi PEDRA e você PAPEL')
elif opcao == 3: #tesoura
    if comp == 3:
        print('Deu EMPATE! Nós dois escolhemos TESOURA!')
    elif comp == 1:
        print('Eu VENCI!! Eu escolhi PEDRA e você TESOURA')
    else:
        print('Você VENCEU!!! Eu escolhi PAPEL e você TESOURA')
else:
    print('Opção inválida! Tente novamente!')
