lista = []
cont_list = cont_item = 1
print('=' * 20)
print('LISTA DE ITENS')
print('=' * 20)
while True:
    print(f'Criando a {cont_list}° lista: ',end='--> ')
    item = str(input(f'{cont_item}° ITEM: ')).upper()
    stop = str(input('CONTINUAR ou PARAR ou nova lista ?[C]/[P]/[N] ')).upper()[0]
    lista.append(item)
    cont_item += 1
    if stop == 'N':
        print(lista)
        lista.append(item)
        lista = []
        cont_list += 1
        print('=' * 20)
        print('LISTA DE ITENS')
        print('=' * 20)
        cont_item = 1
        print('{}°- {}'.format(cont_list, lista))
        continue
    if stop == 'C':
        print(lista)
        continue
    if stop == 'P':
        print('\033[1;34m{}°- {}'.format(cont_list,lista))
        break
    else:
        print('\033[1;31mERROR')
        print('Opção invalida\033[0;0m')
        continuar = str(input('deseja continuar ? [S/N] ')).upper()
        if continuar == 'S':
            continue
        else:
            print("Seus itens foram :\033[1;36m",lista)
            break