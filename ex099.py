from time import sleep


def maior(* num):
    print('=' * 40)
    print('Analisando os valores passados...')
    for i in num:
        print(i, end=' ')
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    if len(num) == 0:
        mai = 0
    else:
        mai = max(num)
    print(f'O maior valor informado foi {mai}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
