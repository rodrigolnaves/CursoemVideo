from ex115.lib.interface import *
from time import sleep

opcoes_do_menu = {'VER PESSOAS CADASTRADAS', 'CADASTRAR NOVA PESSOA', 'SAIR DO SISTEMA'}
while True:
    opc = menu(opcoes_do_menu)
    if opc == 1:
        titulo('OPÇÃO 1')
    elif opc == 2:
        titulo('OPÇÃO 2')
    elif opc == 3:
        titulo('SAINDO DO SISTEMA... ATÉ LOGO!')
        break
    else:
        print(f'{cor("vermelho")}ERRO! Digite uma opção válida.{cor("limpa")}')
    sleep(2)
